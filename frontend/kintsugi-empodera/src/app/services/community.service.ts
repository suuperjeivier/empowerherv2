import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { 
  CommunityPost, 
  CommunityPostCreate, 
  EmotionalLog, 
  EmotionalLogCreate,
  Notification,
  DailyPhrase
} from '../models/community.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CommunityService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // Community Posts
  getCommunityPosts(skip: number = 0, limit: number = 50): Observable<CommunityPost[]> {
    return this.http.get<CommunityPost[]>(`${this.apiUrl}/api/community?skip=${skip}&limit=${limit}`);
  }

  createPost(post: CommunityPostCreate): Observable<CommunityPost> {
    return this.http.post<CommunityPost>(`${this.apiUrl}/api/community`, post);
  }

  deletePost(postId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/api/community/${postId}`);
  }

  // Emotional Tracking
  getEmotionalLogs(skip: number = 0, limit: number = 30): Observable<EmotionalLog[]> {
    return this.http.get<EmotionalLog[]>(`${this.apiUrl}/api/emotional?skip=${skip}&limit=${limit}`);
  }

  createEmotionalLog(log: EmotionalLogCreate): Observable<EmotionalLog> {
    return this.http.post<EmotionalLog>(`${this.apiUrl}/api/emotional`, log);
  }

  // Notifications
  getNotifications(skip: number = 0, limit: number = 50): Observable<Notification[]> {
    return this.http.get<Notification[]>(`${this.apiUrl}/api/notifications?skip=${skip}&limit=${limit}`);
  }

  markNotificationAsRead(notificationId: number): Observable<Notification> {
    return this.http.put<Notification>(`${this.apiUrl}/api/notifications/${notificationId}/read`, {});
  }

  markAllNotificationsAsRead(): Observable<any> {
    return this.http.put(`${this.apiUrl}/api/notifications/read-all`, {});
  }

  // Daily Phrases
  getTodayPhrase(): Observable<DailyPhrase> {
    return this.http.get<DailyPhrase>(`${this.apiUrl}/api/daily-phrases/today`);
  }

  getAllPhrases(skip: number = 0, limit: number = 100): Observable<DailyPhrase[]> {
    return this.http.get<DailyPhrase[]>(`${this.apiUrl}/api/daily-phrases?skip=${skip}&limit=${limit}`);
  }
}

// Made with Bob
