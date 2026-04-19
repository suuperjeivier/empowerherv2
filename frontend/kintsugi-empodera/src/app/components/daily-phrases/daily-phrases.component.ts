import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CommunityService } from '../../services/community.service';
import { DailyPhrase } from '../../models/community.model';

@Component({
  selector: 'app-daily-phrases',
  standalone: true,
  imports: [CommonModule],
  template: '<div class="phrases-container"><h1>Frases Diarias</h1><p *ngIf="todayPhrase">{{ todayPhrase.phrase }}</p></div>',
  styles: ['.phrases-container { padding: 2rem; }']
})
export class DailyPhrasesComponent implements OnInit {
  todayPhrase: DailyPhrase | null = null;
  allPhrases: DailyPhrase[] = [];

  constructor(private communityService: CommunityService) {}

  ngOnInit(): void {
    this.communityService.getTodayPhrase().subscribe({
      next: (phrase) => this.todayPhrase = phrase,
      error: (error) => console.error('Error loading phrase:', error)
    });
  }
}

// Made with Bob
