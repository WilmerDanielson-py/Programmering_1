// Utility-funktioner för att ladda sprites och skapa spelobjekt
function loadSprite(src) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.src = src + "?t=" + new Date().getTime();
        img.onload = () => resolve(img);
        img.onerror = (err) => reject(err);
    })
}

function makeSprite(c, sprite, pos, scale = 1) {
    return {
        width: sprite.width,
        height: sprite.height,
        pos,
        scale,
        draw() {
            c.drawImage(
                sprite,
                this.pos.x,
                this.pos.y,
                this.width * scale,
                this.height * scale
            );
       },
    };
}
function makeLayer(c, sprite, pos, scale = 1) {
    return {
        head: makeSprite(c, sprite, pos, scale),
        tail: makeSprite(c, sprite, { x: pos.x + sprite.width * scale, y: pos.y }, scale),
    };


}

function makeInfiniteScroll(dt, layer, speed) {

    layer.head.pos.x += speed * dt;
    layer.tail.pos.x += speed * dt;

    const width = layer.head.width * layer.head.scale;

    // Om scrolla vänster
    if (speed < 0) {
        if (layer.head.pos.x + width < 0) {
            layer.head.pos.x = layer.tail.pos.x + width;
        }
        if (layer.tail.pos.x + width < 0) {
            layer.tail.pos.x = layer.head.pos.x + width;
        }
    }

    // Om scrolla höger
    if (speed > 0) {
        if (layer.head.pos.x > width) {
            layer.head.pos.x = layer.tail.pos.x - width;
        }
        if (layer.tail.pos.x > width) {
            layer.tail.pos.x = layer.head.pos.x - width;
        }
    }

    layer.head.draw();
    layer.tail.draw();
}