import { Injectable } from '@angular/core';
import { Cars } from './cars';
import { Observable, of } from 'rxjs';
import { ThrowStmt } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})
export class BasketService {

  basket: Cars[] = [];
  constructor() { }

  addCarsToBasket(cars: Cars){
    this.basket.push(cars)
  }

  getCarsFromBasket(): Observable<Cars[]>{
    return of(this.basket)
  }

  deleteCarsFromBasket(cars: Cars){
    for(let i = 0; i < this.basket.length; i++){
      if(this.basket[i].id == cars.id){
        this.basket.splice(i,1)
      }
    }
    this.basket.find(cars => cars.id == cars.id)
  }
}
