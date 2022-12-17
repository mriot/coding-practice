document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#wire-length").addEventListener("change", (event) => {
    vertices.maxWireDist = event.target.value;
  });

  const canvas = document.querySelector("#canvas");
  const dimensions = {
    width: window.innerWidth,
    height: window.innerHeight - 10,
  };
  canvas.width = dimensions.width;
  canvas.height = dimensions.height;
  const ctx = canvas.getContext("2d");

  const vertices = {
    count: 50,
    maxWireDist: 400,
    arcs: [],
  };

  const PaintCanvas = () => {
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, dimensions.width, dimensions.height);
  };

  class Arc {
    constructor(radius = 4) {
      this.x = Math.random() * dimensions.width;
      this.y = Math.random() * dimensions.height;

      this.vx = Math.round(Math.random()) * 2 - 1;
      this.vy = Math.round(Math.random()) * 2 - 1;

      this.radius = radius;

      this.draw = () => {
        ctx.fillStyle = "#fff";
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fill();
      };
    }
  }

  class Wire {
    constructor(x1, y1, x2, y2, color) {
      this.x1 = x1;
      this.y1 = y1;

      this.x2 = x2;
      this.y2 = y2;

      ctx.strokeStyle = color;
      ctx.beginPath();
      ctx.moveTo(this.x1, this.y1);
      ctx.lineTo(this.x2, this.y2);
      // ctx.bezierCurveTo(dimensions.height, dimensions.width / 4, dimensions.width / 2, dimensions.height / 2, this.x2, this.y2);
      // ctx.quadraticCurveTo(dimensions.width / 2, dimensions.height / 2, this.x2, this.y2);
      ctx.stroke();
    }
  }

  const Draw = () => {
    PaintCanvas();

    for (let i = 0; i < vertices.count; i++) {
      // BOUNDARIES
      // right
      if (vertices.arcs[i].x + vertices.arcs[i].radius >= dimensions.width) vertices.arcs[i].vx *= -1;
      // bottom
      if (vertices.arcs[i].y + vertices.arcs[i].radius >= dimensions.height) vertices.arcs[i].vy *= -1;
      // left
      if (vertices.arcs[i].x - vertices.arcs[i].radius <= 0) vertices.arcs[i].vx *= -1;
      // top
      if (vertices.arcs[i].y - vertices.arcs[i].radius <= 0) vertices.arcs[i].vy *= -1;

      if (
        vertices.arcs[i].x < 0 ||
        vertices.arcs[i].x > dimensions.width ||
        vertices.arcs[i].y < 0 ||
        vertices.arcs[i].y > dimensions.height
      ) {
        vertices.arcs[i].x = dimensions.width / 2;
        vertices.arcs[i].y = dimensions.height / 2;
      }

      vertices.arcs[i].x += vertices.arcs[i].vx;
      vertices.arcs[i].y += vertices.arcs[i].vy;

      for (let j = i; j < vertices.count; j++) {
        const distX = vertices.arcs[i].x - vertices.arcs[j].x;
        const distY = vertices.arcs[i].y - vertices.arcs[j].y;

        const dist = Math.sqrt(Math.pow(distX, 2) + Math.pow(distY, 2));

        if (dist <= vertices.maxWireDist) {
          const fraction = dist / vertices.maxWireDist;
          new Wire(
            vertices.arcs[i].x,
            vertices.arcs[i].y,
            vertices.arcs[j].x,
            vertices.arcs[j].y,
            `rgba(255, 0, 0, ${1 - fraction})`
          );
        }

        // if (dist < vertices.arcs[i].radius + vertices.arcs[j].radius) {
        // 	vertices.arcs[i].vx *= -1;
        // 	vertices.arcs[j].vx *= -1;
        // 	vertices.arcs[i].vy *= -1;
        // 	vertices.arcs[j].vy *= -1;
        // }
      }

      vertices.arcs[i].draw();
    }
  };

  document.addEventListener("mousemove", (e) => {
    vertices.arcs[0].vx = 0;
    vertices.arcs[0].vy = 0;
    vertices.arcs[0].x = e.pageX;
    vertices.arcs[0].y = e.pageY;
  });

  document.addEventListener("click", (e) => {
    const arc = new Arc();
    arc.x = e.pageX;
    arc.y = e.pageY;
    vertices.arcs.push(arc);
    vertices.count++;
  });

  for (let i = 0; i < vertices.count; i++) {
    vertices.arcs.push(new Arc());
    vertices.arcs[i].draw();
  }

  const Animloop = () => {
    Draw();
    requestAnimationFrame(Animloop);
  };

  Animloop();
});
