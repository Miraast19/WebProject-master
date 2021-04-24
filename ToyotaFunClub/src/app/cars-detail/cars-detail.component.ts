import { Component, OnInit } from '@angular/core';
import { Cars } from '../cars';
import { CarsListService } from '../cars-list.service';
import { ActivatedRoute } from "@angular/router";
import { BasketService } from '../basket.service';
@Component({
  selector: 'app-cars-detail',
  templateUrl: './cars-detail.component.html',
  styleUrls: ['./cars-detail.component.css']
})
export class CarsDetailComponent implements OnInit {

  carsList: Cars[]
  selectedCarsId: String

  constructor(private route: ActivatedRoute, private carsListService: CarsListService, private basketService: BasketService) { }

  ngOnInit(): void {
    this.getCarsList()
    this.route.paramMap.subscribe(params => {
      this.selectedCarsId = params.get("carsId")
    })
  }

  getCarsList(): void {
    this.carsListService.getCarsList().subscribe( cars => this.carsList = cars)
  }

  onAddToBasket(cars: Cars): void {
    this.basketService.addCarsToBasket(cars)
  }

}
