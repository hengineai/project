function render(scene) {
  requestAnimationFrame(() => render(scene));
  updateScene(scene);
  drawScene(scene);
}

function updateScene(scene) {
  // Update object positions, animations, etc.
  scene.objects.forEach(obj => {
    obj.rotation += 0.01;
  });
}

function drawScene(scene) {
  const ctx = scene.canvas.getContext('2d');
  ctx.clearRect(0, 0, scene.canvas.width, scene.canvas.height);
  scene.objects.forEach(obj => {
    ctx.save();
    ctx.translate(obj.x, obj.y);
    ctx.rotate(obj.rotation);
    ctx.fillStyle = obj.color;
    ctx.fillRect(-obj.size/2, -obj.size/2, obj.size, obj.size);
    ctx.restore();
  });
}
