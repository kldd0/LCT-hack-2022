import {PlacementType} from "./placement-type";

export class PickPoint {
  constructor(public position: google.maps.LatLngLiteral, public options: google.maps.MarkerOptions = {draggable: false, clickable: true}, private demand: number = 0, private placement: PlacementType = PlacementType.None) {
  }
}
