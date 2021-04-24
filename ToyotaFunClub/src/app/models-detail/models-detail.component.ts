import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Model } from '../model';
import { ModelsService } from '../models.service';

@Component({
  selector: 'app-models-detail',
  templateUrl: './models-detail.component.html',
  styleUrls: ['./models-detail.component.css']
})
export class ModelsDetailComponent implements OnInit {

  constructor(private route: ActivatedRoute, private modelsService: ModelsService) { }

  models: Model[]

  ngOnInit(): void {
    this.getModels()
  }

  getModels(): void {
    this.modelsService.getModels().subscribe( models => this.models = models)
  }

}
