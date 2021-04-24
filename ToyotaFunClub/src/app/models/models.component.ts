import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Model } from '../model';
import { ModelsService } from '../models.service';

@Component({
  selector: 'app-models',
  templateUrl: './models.component.html',
  styleUrls: ['./models.component.css']
})
export class ModelsComponent implements OnInit {

  constructor(private route: ActivatedRoute, private modelsService: ModelsService) { }

  models: Model[]

  ngOnInit(): void {
    this.getModels()
  }

  getModels(): void {
    this.modelsService.getModels().subscribe( models => this.models = models)
  }
}
