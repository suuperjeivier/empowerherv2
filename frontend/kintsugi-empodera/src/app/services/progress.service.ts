import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Progress, DashboardStats } from '../models/course.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProgressService {
  private apiUrl = `${environment.apiUrl}/api/progress`;

  constructor(private http: HttpClient) {}

  updateProgress(moduleId: number, isCompleted: boolean): Observable<Progress> {
    return this.http.post<Progress>(this.apiUrl, {
      module_id: moduleId,
      is_completed: isCompleted
    });
  }

  getDashboardStats(): Observable<DashboardStats> {
    return this.http.get<DashboardStats>(`${this.apiUrl}/dashboard`);
  }
}

// Made with Bob
