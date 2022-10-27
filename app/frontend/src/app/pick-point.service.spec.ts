import { TestBed } from '@angular/core/testing';

import { PickPointService } from './pick-point.service';

describe('PickPointService', () => {
  let service: PickPointService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PickPointService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
