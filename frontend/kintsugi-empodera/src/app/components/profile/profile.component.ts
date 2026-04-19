import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="profile-container"><h1>Perfil</h1><p *ngIf="currentUser">{{ currentUser.full_name || currentUser.username }}</p></div>',
  styles: ['.profile-container { padding: 2rem; }']
})
export class ProfileComponent implements OnInit {
  currentUser: User | null = null;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    this.authService.currentUser.subscribe(user => {
      this.currentUser = user;
    });
  }
}

// Made with Bob
