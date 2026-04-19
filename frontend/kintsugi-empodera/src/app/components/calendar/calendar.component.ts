import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-calendar',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="calendar-container"><h1>Calendario & Planificador</h1><p>Organiza tus actividades de aprendizaje</p></div>',
  styles: ['.calendar-container { padding: 2rem; }']
})
export class CalendarComponent {}

// Made with Bob
