import { Injectable } from '@angular/core';
import { Model } from './model';
import { MODELS} from './models-list';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ModelsService {

  models = MODELS

  getModels(): Observable<Model[]> {
    return of(MODELS);
  }
  constructor() { }
}
