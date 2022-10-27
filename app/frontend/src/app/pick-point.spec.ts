import { PickPoint } from './pick-point';

describe('PickPoint', () => {
  let test: PickPoint;

  beforeAll(() => {
    test = new PickPoint({lat: 0, lng: 0})
  })

  it('should create an instance', () => {
    expect(test).toBeTruthy();
  });

  it("should be clickable", () => {
    expect(test.options.clickable).toBeTrue()
  });

  it("shouldn't be draggable", () => {
    expect(test.options.draggable).toBeFalse();
  })
});
