import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { CourseService } from '../../services/course.service';
import { ProgressService } from '../../services/progress.service';
import { CommunityService } from '../../services/community.service';
import { User } from '../../models/user.model';
import { CourseProgress, DashboardStats } from '../../models/course.model';
import { DailyPhrase } from '../../models/community.model';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  private readonly MAX_DISPLAYED_COURSES = 3;
  
  currentUser: User | null = null;
  dashboardStats: DashboardStats | null = null;
  myCourses: CourseProgress[] = [];
  dailyPhrase: DailyPhrase | null = null;
  isLoading = true;

  constructor(
    private authService: AuthService,
    private courseService: CourseService,
    private progressService: ProgressService,
    private communityService: CommunityService
  ) {}

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.authService.currentUser.subscribe(user => {
      this.currentUser = user;
    });

    this.progressService.getDashboardStats().subscribe({
      next: (stats) => {
        this.dashboardStats = stats;
      },
      error: (error) => console.error('Error loading stats:', error)
    });

    this.courseService.getMyCourses().subscribe({
      next: (courses) => {
        this.myCourses = courses.slice(0, this.MAX_DISPLAYED_COURSES);
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Error loading courses:', error);
        this.isLoading = false;
      }
    });

    this.communityService.getTodayPhrase().subscribe({
      next: (phrase) => {
        this.dailyPhrase = phrase;
      },
      error: (error) => console.error('Error loading daily phrase:', error)
    });
  }

  logout(): void {
    this.authService.logout();
  }
}

// Made with Bob
