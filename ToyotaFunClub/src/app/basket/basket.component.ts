import { Component, OnInit } from '@angular/core';
import { BasketService } from '../basket.service';
import { Cars } from '../cars';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrls: ['./basket.component.css']
})
export class BasketComponent implements OnInit {

  carsFromBasket: Cars[] = [];

  constructor(private basketService: BasketService) { }

  ngOnInit(): void {
    this.getCarsFromBasket()
  }

  getCarsFromBasket(): void {
    this.basketService.getCarsFromBasket().subscribe( cars => this.carsFromBasket = cars)
  }

  deleteCarsFromBasket(cars: Cars) {
    this.basketService.deleteCarsFromBasket(cars)
  }
  buyCarsFromBasket(cars: Cars)
  {
    this.basketService.deleteCarsFromBasket(cars)
    window.alert('Congratulations!!! You are now Toyota car owner!')
  }
}
