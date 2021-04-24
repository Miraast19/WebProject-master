import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Model } from './model';
@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService{
  // createDb(){
    // const model: Model[]=[]
  // }
  constructor() { }
  createDb(reqInfo?: import("angular-in-memory-web-api").RequestInfo): {} | import("rxjs").Observable<{}> | Promise<{}> {
    throw new Error("Method not implemented.");
    const model= [ {id: 1, name: "Corolla"},
    {id: 2, name: "Camry"},
    {id: 3, name: "Avalon"},
    {id: 4, name: "Rav4"},
    {id: 5, name: "Highlander"},
    {id: 6, name: "Land Cruiser"},
    {id: 7, name: "Sequoia"}];
    return{model};
  }
}
