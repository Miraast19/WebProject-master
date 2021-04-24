import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ModelsComponent } from './models/models.component';
import { CarsListComponent } from './cars-list/cars-list.component';
import { HomeComponent } from './home/home.component';
import { RoutingComponent } from './routing/routing.component';
import { CarsDetailComponent } from './cars-detail/cars-detail.component';
import { BasketComponent } from './basket/basket.component';
import { CarComponent } from './car/car.component';
import { ModelsDetailComponent } from './models-detail/models-detail.component';
import { LoginComponent } from './login/login.component';
import { ProductServiceComponent } from './product-service/product-service.component';
import { SignUpComponent } from './sign-up/sign-up.component';

@NgModule({
  declarations: [
    AppComponent,
    ModelsComponent,
    CarsListComponent,
    HomeComponent,
    RoutingComponent,
    CarsDetailComponent,
    BasketComponent,
    CarComponent,
    ModelsDetailComponent,
    LoginComponent,
    ProductServiceComponent,
    SignUpComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
