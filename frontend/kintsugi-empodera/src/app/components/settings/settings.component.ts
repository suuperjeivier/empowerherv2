import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="settings-container"><h1>Ajustes</h1><p>Configura tu experiencia</p><button (click)="logout()" class="btn-primary">Cerrar Sesión</button></div>',
  styles: ['.settings-container { padding: 2rem; }']
})
export class SettingsComponent {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}

// Made with Bob
