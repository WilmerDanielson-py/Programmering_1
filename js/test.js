
const IdleWIZARD = document.getElementById("IdleWIZARD");
const RunWIZARD = document.getElementById("RunWIZARD");
const JumpWIZARD = document.getElementById("JumpWIZARD");
const FallWIZARD = document.getElementById("FallWIZARD");
const AttackWIZARD = document.getElementById("AttackWIZARD");
const MovingWIZARD = document.getElementById("MovingWIZARD");
const ExplodeWIZARD = document.getElementById("ExplodeWIZARD");


let projectiles = [];
let current = IdleWIZARD;


let testHitbox = {
    x: 600,
    y: 300,
    width: 100,
    height: 100
};


let hitEffects = [];

const spriteWidth = 140;
const spriteHeight = 150;
const scale = 2;

const renderWidth = spriteWidth * scale;
const renderHeight = spriteHeight * scale;

const explodeSpriteWidth = 50;
const explodeSpriteHeight = 50;
const explodeScale = 2;

const explodeRenderWidth = explodeSpriteWidth * explodeScale;
const explodeRenderHeight = explodeSpriteHeight * explodeScale;

// Animation
let frameIndex = 0;
let totalFrames = 10;

let lastTimestamp = 0;
const maxFPS = 15;
const timestep = 1000 / maxFPS;

// Projektil animation
const projectileFrames = 4;
const projectileSpriteWidth = 50;
const projectileSpriteHeight = 50;
const projectileScale = 1.5; 



let isAttacking = false;
let attackState = 0; 
let attackFrames = 13;
let canAttack = true;

// Fysik
const GRAVITY = 1.2;

let x = canvas.width / 2;
let y = canvas.height - renderHeight;

const groundY = canvas.height;

let player = {
    speed: 8,
    JumpWIZARDForce: 22,
    velocityY: 0,
    onGround: true,
    facing: 1, 

    hitboxProjectile: {
        width: 40,
        height: 20,
        offsetX: 170,
        offsetY: 75
    },  

    hitbox: {
        width: 80,
        height: 110,
        offsetX: 100,
        offsetY: 85
    },

    direction: {
        left: false,
        right: false
    }
};

// Olika input för att hantera både tangentbord och mus
document.addEventListener("keydown", (e) => {

    if (e.code === "Space" && player.onGround) {
        player.velocityY = -player.JumpWIZARDForce;
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


document.addEventListener("mousedown", (e) => {
    if (e.button === 0 && canAttack) {
        if (attackState === 0) {
            // Starta AttackWIZARD
            attackState = 1;
            isAttacking = true;
            frameIndex = 0;
            canAttack = false;
        
        }
    }
});

function shootProjectile() {

    let startX;

    if (player.facing === 1) {
        startX = x + player.hitboxProjectile.offsetX;
    } else {
        startX = x + renderWidth - player.hitboxProjectile.offsetX;
    }

    projectiles.push({
        x: startX,
        y: y + player.hitboxProjectile.offsetY,
        width: projectileSpriteWidth * projectileScale,
        height: projectileSpriteHeight * projectileScale,
        hitboxWidth: 30,
        hitboxHeight: 20,
        hitboxOffsetX: (projectileSpriteWidth * projectileScale - 30) / 2,
        hitboxOffsetY: (projectileSpriteHeight * projectileScale - 20) / 2,
        speed: 12 * player.facing,
        frameIndex: 0,
        direction: player.facing
    });
}

function showHitEffect(hitX, hitY) {
    hitEffects.push({
        x: hitX,
        y: hitY,  
        offsetX: -explodeRenderWidth / 2,
        offsetY: -explodeRenderHeight / 2,
        frameIndex: 0,
        totalFrames: 7,
        sprite: ExplodeWIZARD
    });
}
// Updatera position och animation varje frame
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

    // Markkollision
    let hitboxBottom = y + player.hitbox.offsetY + player.hitbox.height;

    if (hitboxBottom >= groundY) {
        y = groundY - player.hitbox.height - player.hitbox.offsetY;
        player.velocityY = 0;
        player.onGround = true;
    }
    

    // Animation state
    if (isAttacking) {
        if (attackState === 1) {
            current = AttackWIZARD;
            totalFrames = 13;
        }
    } else if (!player.onGround) {
        if (player.velocityY < 0) {
            current = JumpWIZARD;
            totalFrames = 3;
        } else {
            current = FallWIZARD;
            totalFrames = 3;
        }
    } else {
        if (player.direction.left || player.direction.right) {
            current = RunWIZARD;
            totalFrames = 8;
        } else {
            current = IdleWIZARD;
            totalFrames = 10;
        }
    }

    for (let i = 0; i < projectiles.length; i++) {

    let p = projectiles[i];

    // flytta projektilen
    p.x += p.speed;
    
    // uppdatera projektilens animation
    p.frameIndex = (p.frameIndex + 1) % projectileFrames;

    // ta bort projektilen utanför skärmen
    if (p.x < -100 || p.x > canvas.width + 100) {
        projectiles.splice(i,1);
        i--;
    }
}
    
    // Kollision mellan projektiler och test-hitbox
    for (let i = projectiles.length - 1; i >= 0; i--) {
        let p = projectiles[i];
        
        if (p.x + p.hitboxOffsetX < testHitbox.x + testHitbox.width &&
            p.x + p.hitboxOffsetX + p.hitboxWidth > testHitbox.x &&
            p.y + p.hitboxOffsetY < testHitbox.y + testHitbox.height &&
            p.y + p.hitboxOffsetY + p.hitboxHeight > testHitbox.y) {
            
            // Träff registrerad!
            console.log("Träff på test-hitbox!");
            
            // Ta bort projektilen efter träff
            projectiles.splice(i, 1);
            
            // Visa effekt med ExplodeWIZARD
            showHitEffect(
                p.x + p.hitboxOffsetX + p.hitboxWidth / 2,
                p.y + p.hitboxOffsetY + p.hitboxHeight / 2,
                p.hitboxHeight
            );
        }
    }
    
    // Uppdatera effekter
    for (let i = hitEffects.length - 1; i >= 0; i--) {
        let effect = hitEffects[i];
        effect.frameIndex++;
        
        // Ta bort effekten
        if (effect.frameIndex >= effect.totalFrames) {
            hitEffects.splice(i, 1);
        }
    } 
}


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

    // spelar hitbox
    ctx.strokeStyle = "lime";
    ctx.strokeRect(
        x + player.hitbox.offsetX,
        y + player.hitbox.offsetY,
        player.hitbox.width,
        player.hitbox.height
    );

    if (player.facing === 1) {
        hitboxX = x + player.hitboxProjectile.offsetX;
    } else {
        hitboxX = x + renderWidth - player.hitboxProjectile.offsetX - player.hitboxProjectile.width;
    }

    
    for (let p of projectiles) {

    ctx.save();

    // Spegelvända projektilen om den åker åt vänster
    if (p.direction === -1) {
        ctx.translate(p.x + (projectileSpriteWidth * projectileScale) / 2, p.y);
        ctx.scale(-1, 1);
        ctx.translate(-(p.x + (projectileSpriteWidth * projectileScale) / 2), -p.y);
    }

    ctx.drawImage(
        MovingWIZARD,
        p.frameIndex * projectileSpriteWidth,
        0,
        projectileSpriteWidth,
        projectileSpriteHeight,
        p.x,
        p.y,
        projectileSpriteWidth * projectileScale,
        projectileSpriteHeight * projectileScale
    );

    ctx.restore();

    //Projektilens hitbox
    ctx.strokeStyle = "blue";
    ctx.strokeRect(p.x + p.hitboxOffsetX, p.y + p.hitboxOffsetY, p.hitboxWidth, p.hitboxHeight);
    }
    

    //Test hitbox
    ctx.strokeStyle = "red";
    ctx.strokeRect(testHitbox.x, testHitbox.y, testHitbox.width, testHitbox.height);

    
    for (let effect of hitEffects) {
        ctx.drawImage(
            effect.sprite,
            effect.frameIndex * explodeSpriteWidth, 
            0,
            explodeSpriteWidth,
            explodeSpriteHeight,
            effect.x + effect.offsetX,  // Använd offset för centrering
            effect.y + effect.offsetY,
            explodeRenderWidth,
            explodeRenderHeight
        );
    }
}


function gameLooptest(timestamp) {

    if (timestamp - lastTimestamp > timestep) {
        frameIndex = (frameIndex + 1) % totalFrames;
        lastTimestamp = timestamp;

        // Skjut projektil
        if (isAttacking && attackState === 1 && frameIndex === totalFrames - 5) {
            shootProjectile();
        }

        // Hantera attack
        if (isAttacking && frameIndex === 0) {
            if (attackState === 1) {
                
                isAttacking = false;
                attackState = 0;
                canAttack = true; 
            
            }
        }
    }

    update();
    draw();

    requestAnimationFrame(gameLooptest);
}

