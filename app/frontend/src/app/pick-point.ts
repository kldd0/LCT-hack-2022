import {PlacementType} from "./placement-type";

export class PickPoint {
  constructor(public position: google.maps.LatLngLiteral, public options: google.maps.MarkerOptions = {draggable: false, clickable: true}, private demand = 0, private placement = PlacementType.None) {
  }
}
