import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Course, Module, Enrollment, CourseProgress } from '../models/course.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private apiUrl = `${environment.apiUrl}/api/courses`;

  constructor(private http: HttpClient) {}

  getCourses(): Observable<Course[]> {
    return this.http.get<Course[]>(this.apiUrl);
  }

  getCourse(id: number): Observable<Course> {
    return this.http.get<Course>(`${this.apiUrl}/${id}`);
  }

  getCourseModules(courseId: number): Observable<Module[]> {
    return this.http.get<Module[]>(`${this.apiUrl}/${courseId}/modules`);
  }

  enrollInCourse(courseId: number): Observable<Enrollment> {
    return this.http.post<Enrollment>(`${this.apiUrl}/enroll`, { course_id: courseId });
  }

  getMyCourses(): Observable<CourseProgress[]> {
    return this.http.get<CourseProgress[]>(`${this.apiUrl}/my-courses`);
  }
}

// Made with Bob
