import { Component, OnInit } from '@angular/core';
import { Cars } from '../cars';
import { CarsListService } from '../cars-list.service';
import { BasketService } from '../basket.service';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-cars-list',
  templateUrl: './cars-list.component.html',
  styleUrls: ['./cars-list.component.css']
})
export class CarsListComponent implements OnInit {

  constructor(private route: ActivatedRoute, private carsListService: CarsListService, private basketService: BasketService) { }
  
  carsList: Cars[]

  ngOnInit(): void {
    this.getCarsList()
  }

  selectedCars: Cars

  getCarsList(): void {
    this.carsListService.getCarsList().subscribe( cars => this.carsList = cars)
  }

  onAddToBasket(cars: Cars): void {
    this.basketService.addCarsToBasket(cars)
    window.alert('Added to the basket!')
  }

  onSelect(cars: Cars): void{
    this.selectedCars = cars;
  }

}
