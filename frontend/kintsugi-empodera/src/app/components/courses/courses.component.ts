import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { CourseService } from '../../services/course.service';
import { Course, CourseProgress } from '../../models/course.model';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './courses.component.html',
  styleUrl: './courses.component.scss'
})
export class CoursesComponent implements OnInit {
  allCourses: Course[] = [];
  myCourses: CourseProgress[] = [];
  filteredCourses: Course[] = [];
  isLoading = true;
  selectedTab: 'all' | 'in-progress' | 'completed' = 'all';

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {
    this.loadCourses();
  }

  loadCourses(): void {
    // Load all courses
    this.courseService.getCourses().subscribe({
      next: (courses: Course[]) => {
        this.allCourses = courses;
        this.filterCourses();
      },
      error: (error: any) => {
        console.error('Error loading courses:', error);
      }
    });

    // Load user's enrolled courses
    this.courseService.getMyCourses().subscribe({
      next: (courses: CourseProgress[]) => {
        this.myCourses = courses;
        this.filterCourses();
        this.isLoading = false;
      },
      error: (error: any) => {
        console.error('Error loading my courses:', error);
        this.isLoading = false;
      }
    });
  }

  selectTab(tab: 'all' | 'in-progress' | 'completed'): void {
    this.selectedTab = tab;
    this.filterCourses();
  }

  filterCourses(): void {
    switch (this.selectedTab) {
      case 'all':
        this.filteredCourses = this.allCourses;
        break;
      case 'in-progress':
        // Show courses that are enrolled but not 100% complete
        const inProgressIds = this.myCourses
          .filter(cp => cp.progress_percentage < 100)
          .map(cp => cp.course.id);
        this.filteredCourses = this.allCourses.filter(course =>
          inProgressIds.includes(course.id)
        );
        break;
      case 'completed':
        // Show courses that are 100% complete
        const completedIds = this.myCourses
          .filter(cp => cp.progress_percentage === 100)
          .map(cp => cp.course.id);
        this.filteredCourses = this.allCourses.filter(course =>
          completedIds.includes(course.id)
        );
        break;
    }
  }

  getCourseProgress(courseId: number): number {
    const courseProgress = this.myCourses.find(cp => cp.course.id === courseId);
    return courseProgress ? courseProgress.progress_percentage : 0;
  }

  isEnrolled(courseId: number): boolean {
    return this.myCourses.some(cp => cp.course.id === courseId);
  }

  trackByCourseId(index: number, course: Course): number {
    return course.id;
  }
}

// Made with Bob
