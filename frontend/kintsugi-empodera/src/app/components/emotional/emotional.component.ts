import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CommunityService } from '../../services/community.service';
import { EmotionalLog, EmotionalState } from '../../models/community.model';

@Component({
  selector: 'app-emotional',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: '<div class="emotional-container"><h1>Estado Emocional</h1><p>¿Cómo te sientes hoy?</p></div>',
  styles: ['.emotional-container { padding: 2rem; }']
})
export class EmotionalComponent implements OnInit {
  logs: EmotionalLog[] = [];
  selectedState: EmotionalState = 'happy';
  note = '';

  constructor(private communityService: CommunityService) {}

  ngOnInit(): void {
    this.loadLogs();
  }

  loadLogs(): void {
    this.communityService.getEmotionalLogs().subscribe({
      next: (logs) => this.logs = logs,
      error: (error) => console.error('Error loading logs:', error)
    });
  }

  saveLog(): void {
    this.communityService.createEmotionalLog({ emotional_state: this.selectedState, note: this.note }).subscribe({
      next: () => {
        this.note = '';
        this.loadLogs();
      },
      error: (error) => console.error('Error saving log:', error)
    });
  }
}

// Made with Bob
