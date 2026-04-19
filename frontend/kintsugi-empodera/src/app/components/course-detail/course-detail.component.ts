import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CourseService } from '../../services/course.service';
import { ProgressService } from '../../services/progress.service';
import { Course, Module } from '../../models/course.model';

@Component({
  selector: 'app-course-detail',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './course-detail.component.html',
  styleUrl: './course-detail.component.scss'
})
export class CourseDetailComponent implements OnInit {
  course: Course | null = null;
  modules: Module[] = [];
  isLoading = true;

  constructor(
    private route: ActivatedRoute,
    private courseService: CourseService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    const courseId = Number(this.route.snapshot.paramMap.get('id'));
    this.loadCourseDetails(courseId);
  }

  loadCourseDetails(courseId: number): void {
    this.courseService.getCourse(courseId).subscribe({
      next: (course) => {
        this.course = course;
      },
      error: (error) => console.error('Error loading course:', error)
    });

    this.courseService.getCourseModules(courseId).subscribe({
      next: (modules) => {
        this.modules = modules;
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Error loading modules:', error);
        this.isLoading = false;
      }
    });
  }

  toggleModuleComplete(moduleId: number, isCompleted: boolean): void {
    this.progressService.updateProgress(moduleId, !isCompleted).subscribe({
      next: () => {
        const module = this.modules.find(m => m.id === moduleId);
        if (module) {
          // Refresh the page or update local state
          this.loadCourseDetails(this.course!.id);
        }
      },
      error: (error) => console.error('Error updating progress:', error)
    });
  }
}

// Made with Bob
