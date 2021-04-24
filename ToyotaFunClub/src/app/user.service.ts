import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from './User';
import { USERS } from './users';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  getUsers(): Observable<User[]> {
    return of(USERS);
  }

  getUser(username: String): Observable<User> {
    return of(USERS.find(user => user.username === username));
  }

  register(user: User){
    USERS.push(user);
  }

  
}