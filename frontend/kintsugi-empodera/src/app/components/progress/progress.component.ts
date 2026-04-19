import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProgressService } from '../../services/progress.service';
import { CourseService } from '../../services/course.service';
import { DashboardStats, CourseProgress } from '../../models/course.model';

@Component({
  selector: 'app-progress',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './progress.component.html',
  styleUrl: './progress.component.scss'
})
export class ProgressComponent implements OnInit {
  stats: DashboardStats | null = null;
  courses: CourseProgress[] = [];
  isLoading = true;

  constructor(
    private progressService: ProgressService,
    private courseService: CourseService
  ) {}

  ngOnInit(): void {
    this.loadProgress();
  }

  loadProgress(): void {
    this.progressService.getDashboardStats().subscribe({
      next: (stats) => {
        this.stats = stats;
      },
      error: (error) => console.error('Error loading stats:', error)
    });

    this.courseService.getMyCourses().subscribe({
      next: (courses) => {
        this.courses = courses;
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Error loading courses:', error);
        this.isLoading = false;
      }
    });
  }
}

// Made with Bob
