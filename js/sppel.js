const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// === SPRITES ===
const IdleNINJA = document.getElementById("IdleNINJA");
const RunNINJA = document.getElementById("RunNINJA");
const JumpNINJA = document.getElementById("JumpNINJA");
const FallNINJA = document.getElementById("FallNINJA");
const Attack1NINJA = document.getElementById("Attack1NINJA");
const Attack2NINJA = document.getElementById("Attack2NINJA");

let current = IdleNINJA;

// === SPRITE INFO ===
const spriteWidth = 200;
const spriteHeight = 130;
const scale = 2;

const renderWidth = spriteWidth * scale;
const renderHeight = spriteHeight * scale;

// === ANIMATION ===
let frameIndex = 0;
let totalFrames = 4;

let lastTimestamp = 0;
const maxFPS = 15;
const timestep = 1000 / maxFPS;

let isAttacking = false;
let attackState = 0; 
let attackFrames = 4; 
let canAttack = true; 

// === PHYSICS ===
const GRAVITY = 1.2;

let x = canvas.width / 2;
let y = canvas.height - renderHeight;

const groundY = canvas.height;

let player = {
    speed: 8,
    JumpNINJAForce: 22,
    velocityY: 0,
    onGround: true,
    facing: 1, // 1 = right, -1 = left

    hitboxSword: {
        width: 150,
        height: 140,
        offsetX: 210,
        offsetY: 120
    },

    hitbox: {
        width: 80,
        height: 120,
        offsetX: 160,
        offsetY: 140
    },

    direction: {
        left: false,
        right: false
    }
};

// === INPUT ===
document.addEventListener("keydown", (e) => {

    if (e.code === "Space" && player.onGround) {
        player.velocityY = -player.JumpNINJAForce;
        player.onGround = false;
    }

    if (e.code === "KeyA") {
        player.direction.left = true;
        player.facing = -1;
    }

    if (e.code === "KeyD") {
        player.direction.right = true;
        player.facing = 1;
    }
});

document.addEventListener("keyup", (e) => {
    if (e.code === "KeyA") player.direction.left = false;
    if (e.code === "KeyD") player.direction.right = false;
});

// === MOUSE INPUT ===
document.addEventListener("mousedown", (e) => {
    if (e.button === 0 && canAttack) { // Vänsterklick
        if (attackState === 0) {
            // Starta Attack1NINJA
            attackState = 1;
            isAttacking = true;
            frameIndex = 0;
            canAttack = false;
        } else if (attackState === 1) {
            // Combo: Attack2NINJA efter Attack1NINJA
            attackState = 2;
            isAttacking = true;
            frameIndex = 0;
        }
    }
});

// === UPDATE ===
function update() {

    // Rörelse X
    if (player.direction.left && x > -player.hitbox.offsetX) {
        x -= player.speed;
    }

    if (player.direction.right && x < canvas.width - player.hitbox.width - player.hitbox.offsetX) {
        x += player.speed;
    }

    // Gravitation
    player.velocityY += GRAVITY;
    y += player.velocityY;

    // Markkollision (baserad på hitbox)
    let hitboxBottom = y + player.hitbox.offsetY + player.hitbox.height;

    if (hitboxBottom >= groundY) {
        y = groundY - player.hitbox.height - player.hitbox.offsetY;
        player.velocityY = 0;
        player.onGround = true;
    }
    

    // === ANIMATION STATE MACHINE ===
    if (isAttacking) {
        if (attackState === 1) {
            current = Attack1NINJA;
        } else if (attackState === 2) {
            current = Attack2NINJA;
        }
        totalFrames = attackFrames;
    } else if (!player.onGround) {
        if (player.velocityY < 0) {
            current = JumpNINJA;
            totalFrames = 2;
        } else {
            current = FallNINJA;
            totalFrames = 2;
        }
    } else {
        if (player.direction.left || player.direction.right) {
            current = RunNINJA;
            totalFrames = 8;
        } else {
            current = IdleNINJA;
            totalFrames = 4;
        }
    }
}

// === DRAW ===
function draw() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.save();

    if (player.facing === -1) {
        ctx.translate(x + renderWidth / 2, 0);
        ctx.scale(-1, 1);
        ctx.translate(-(x + renderWidth / 2), 0);
    }

    ctx.drawImage(
        current,
        frameIndex * spriteWidth,
        0,
        spriteWidth,
        spriteHeight,
        x,
        y,
        renderWidth,
        renderHeight
    );

    ctx.restore();

    // DEBUG HITBOX
    ctx.strokeStyle = "lime";
    ctx.strokeRect(
        x + player.hitbox.offsetX,
        y + player.hitbox.offsetY,
        player.hitbox.width,
        player.hitbox.height
    );

    let hitboxX;

        if (player.facing === 1) {
            hitboxX = x + player.hitboxSword.offsetX;
        } else {
            hitboxX = x + renderWidth - player.hitboxSword.offsetX - player.hitboxSword.width;
        }

    let hitboxY = y + player.hitboxSword.offsetY;
    ctx.strokeStyle = "red";
    ctx.strokeRect(
        hitboxX, 
        hitboxY, 
        player.hitboxSword.width, 
        player.hitboxSword.height
    );
}

// === GAME LOOP ===
function gameLoop(timestamp) {

    if (timestamp - lastTimestamp > timestep) {
        frameIndex = (frameIndex + 1) % totalFrames;
        lastTimestamp = timestamp;

        // Hantera attack-progression
        if (isAttacking && frameIndex === 0) {
            if (attackState === 1) {
                // Attack1NINJA är klar, vänta på input för Attack2NINJA
                isAttacking = false;
                canAttack = true; // Spelaren kan nu clicla för Attack2NINJA
            } else if (attackState === 2) {
                // Attack2NINJA är klar, attacksekvensen är över
                isAttacking = false;
                attackState = 0;
                canAttack = true;
            }
        }
    }

    update();
    draw();

    requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);