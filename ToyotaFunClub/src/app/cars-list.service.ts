import { Injectable } from '@angular/core';
import { Cars } from './cars';
import { carsList } from './cars-list';
import { Observable, of } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class CarsListService {

  cars = carsList

  getCarsList(): Observable<Cars[]> {
    return of(carsList)
  }
  constructor() { }
}
