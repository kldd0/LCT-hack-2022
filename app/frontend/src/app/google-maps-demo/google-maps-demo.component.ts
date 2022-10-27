import {Component, ViewChild} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import {PickPointService} from "../pick-point.service";
import {MapInfoWindow, MapMarker} from "@angular/google-maps";

@Component({
  selector: 'google-maps-demo',
  templateUrl: './google-maps-demo.component.html',
})
export class GoogleMapsDemoComponent {
  @ViewChild(MapInfoWindow) infoWindow?: MapInfoWindow;
  infoContent = "Empty";
  heatmapToggle = false;
  points = this.pickPointService.getPoints();
  apiLoaded: Observable<boolean>;
  moscowCenter: google.maps.LatLngLiteral = {
    lat: 55.7522,
    lng: 37.6219,
  };

  constructor(httpClient: HttpClient, private pickPointService: PickPointService) {
    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js?key=AIzaSyBaL5D_2_mGN6dVCyFOhEVYwtixv4zfRgs&libraries=visualization', 'callback')
      .pipe(
        map(() => true),
        catchError(() => of(false)),
      );
  }

  centerOn(position: google.maps.MapMouseEvent, marker: MapMarker) {
      this.infoWindow?.open(marker, true);
    }

    positions = this.pickPointService.getPositions();

}
