import { Injectable } from '@angular/core';
import {PickPoint} from "./pick-point";
import {Observable} from "rxjs";
import {map} from "rxjs/operators"

@Injectable({
  providedIn: 'root'
})
export class PickPointService {
  private readonly points: Observable<PickPoint[]>;
  constructor() {
    this.points = new Observable((subscriber) => {
      subscriber.next([
        new PickPoint({lat: 55.75, lng: 37.62}),
      ]);
    })
  }

  getPoints() {
    return this.points;
  }

  getPositions() {
    return this.points.pipe(
      map((points) => points.map((el) => el.position))
    )
  }
}
