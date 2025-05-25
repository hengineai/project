export function createScene(canvas) {
  return {
    canvas: canvas,
    objects: [
      { x: 100, y: 100, size: 50, rotation: 0, color: 'purple' },
      { x: 200, y: 150, size: 30, rotation: 0, color: 'orange' }
    ]
  };
}
