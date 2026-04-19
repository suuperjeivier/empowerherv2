import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CommunityService } from '../../services/community.service';
import { Notification } from '../../models/community.model';

@Component({
  selector: 'app-notifications',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="notifications-container"><h1>Notificaciones</h1><p>Mantente al día con tus actividades</p></div>',
  styles: ['.notifications-container { padding: 2rem; }']
})
export class NotificationsComponent implements OnInit {
  notifications: Notification[] = [];

  constructor(private communityService: CommunityService) {}

  ngOnInit(): void {
    this.communityService.getNotifications().subscribe({
      next: (notifications) => this.notifications = notifications,
      error: (error) => console.error('Error loading notifications:', error)
    });
  }

  markAsRead(id: number): void {
    this.communityService.markNotificationAsRead(id).subscribe({
      next: () => this.ngOnInit(),
      error: (error) => console.error('Error marking as read:', error)
    });
  }
}

// Made with Bob
