import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-onboarding',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './onboarding.component.html',
  styleUrl: './onboarding.component.scss'
})
export class OnboardingComponent {
  currentSlide = 0;
  slides = [
    {
      title: 'Bienvenida',
      subtitle: 'Tu espacio seguro para aprender, crecer y transformar tu historia.',
      description: 'Donde las grietas se convierten en fortaleza.',
      icon: '✨'
    },
    {
      title: 'Aprende',
      subtitle: 'Cursos diseñados para tu crecimiento personal y profesional',
      description: 'Desarrolla nuevas habilidades a tu propio ritmo',
      icon: '📚'
    },
    {
      title: 'Conecta',
      subtitle: 'Únete a una comunidad de mujeres empoderadas',
      description: 'Comparte experiencias y apóyate mutuamente',
      icon: '👥'
    },
    {
      title: 'Transforma',
      subtitle: 'Celebra cada logro en tu camino de transformación',
      description: 'Tu historia merece ser contada con orgullo',
      icon: '🌟'
    }
  ];

  constructor(private router: Router) {}

  nextSlide(): void {
    if (this.currentSlide < this.slides.length - 1) {
      this.currentSlide++;
    } else {
      this.router.navigate(['/login']);
    }
  }

  previousSlide(): void {
    if (this.currentSlide > 0) {
      this.currentSlide--;
    }
  }

  goToSlide(index: number): void {
    this.currentSlide = index;
  }

  skip(): void {
    this.router.navigate(['/login']);
  }
}

// Made with Bob
