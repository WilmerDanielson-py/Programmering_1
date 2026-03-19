const container = document.querySelector(".container");

new ResizeObserver(() => {
    document.documentElement.style.setProperty(
        "--scale",
        Math.min(
            container.parentElement.offsetWidth / container.offsetWidth,
            container.parentElement.offsetHeight / container.offsetHeight
        )
    );

}).observe(container.parentElement);

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const HPbar = document.getElementById("HPbar");
const IdleWIZARD = document.getElementById("IdleWIZARD");
const RunWIZARD = document.getElementById("RunWIZARD");
const JumpWIZARD = document.getElementById("JumpWIZARD");
const FallWIZARD = document.getElementById("FallWIZARD");
const AttackWIZARD = document.getElementById("AttackWIZARD");
const MovingWIZARD = document.getElementById("MovingWIZARD");
const ExplodeWIZARD = document.getElementById("ExplodeWIZARD");


let projectiles = [];
let current = IdleWIZARD;


// let testHitbox = {
//     x: 600,
//     y: 300,
//     width: 100,
//     height: 100
// };

// 
let hitEffects = [];

let paused = false;
// Sprite info
const spriteWidth = 140;
const spriteHeight = 150;
const scale = 3.5;
const renderWidth = spriteWidth * scale;
const renderHeight = spriteHeight * scale;
// explode sprite info
const explodeSpriteWidth = 50;
const explodeSpriteHeight = 50;
const explodeScale = 2;
// explode render size
const explodeRenderWidth = explodeSpriteWidth * explodeScale;
const explodeRenderHeight = explodeSpriteHeight * explodeScale;

// Animation
let frameIndex = 0;
let totalFrames = 10;
let timeStamp = 0;
let lastTimestamp = 0;
const maxFPS = 15;
const timestep = 1000 / maxFPS;

// Projektil animation
const projectileFrames = 4;
const projectileSpriteWidth = 50;
const projectileSpriteHeight = 50;
const projectileScale = 2.5; 

// HPbar
HPbar.width = 112;
const barWidth = 112;
const barHeight = 32;
const barScale = 3;
let hitcounter = 0;


let playerMovement = 0;
// kamera/världsrörelse
let worldX = 0;
let cameraX = 0;
// Attackstate
let isAttacking = false;
let attackState = 0; 
let attackFrames = 13;
let canAttack = true;

// Fysik
const GRAVITY = 0.9;

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
        offsetY: 130
    },  

    hitbox: {
        width: 100,
        height: 190,
        offsetX: 200,
        offsetY: 150
    },

    direction: {
        left: false,
        right: false
    }
};

// Olika input för att hantera både tangentbord och mus

function restartGame() {
    x = canvas.width / 2;
    y = canvas.height - renderHeight;
    worldX = 0;
    projectiles = [];
    hitEffects = [];
}

document.addEventListener("keydown", (e) => {
    if (e.code === "Escape") {
            paused = !paused;
            return;
            
    }
    if (e.code === "KeyR") {
        restartGame();
        paused = false;
    }
    if (e.code === "KeyQ") {
        hitcounter += 1;
        if (hitcounter > 7)
            hitcounter = 7
    }

    if (paused) return;

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
    if (paused) return;
    if (e.code === "KeyA") player.direction.left = false;
    if (e.code === "KeyD") player.direction.right = false;
});


document.addEventListener("mousedown", (e) => {
    if (paused) return;
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
// Ladda shoot sprite
function shootProjectile() {

    let startX;

    if (player.facing === 1) {
        startX = x + player.hitboxProjectile.offsetX*1.8;
    } else {
        startX = x + renderWidth - player.hitboxProjectile.offsetX*2.5;
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

// function showHitEffect(hitX, hitY) {
//     hitEffects.push({
//         x: hitX,
//         y: hitY,  
//         offsetX: -explodeRenderWidth / 2,
//         offsetY: -explodeRenderHeight / 2,
//         frameIndex: 0,
//         totalFrames: 7,
//         sprite: ExplodeWIZARD
//     });
// }

// Updatera position och animation varje frame
function update() {
    playerMovement = 0;
    // Rörelse X
    if (player.direction.left) {
        worldX -= player.speed;
        playerMovement = -player.speed;
    }

    if (player.direction.right) {
        worldX += player.speed;
        playerMovement = player.speed;
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
    
    // // Kollision mellan projektiler och test-hitbox
    // for (let i = projectiles.length - 1; i >= 0; i--) {
    //     let p = projectiles[i];
        
    //     if (p.x + p.hitboxOffsetX < testHitbox.x + testHitbox.width &&
    //         p.x + p.hitboxOffsetX + p.hitboxWidth > testHitbox.x &&
    //         p.y + p.hitboxOffsetY < testHitbox.y + testHitbox.height &&
    //         p.y + p.hitboxOffsetY + p.hitboxHeight > testHitbox.y) {
            
    //         console.log("Träff på test-hitbox!");
            
    //         // Ta bort projektilen efter träff
    //         projectiles.splice(i, 1);
            
    //         showHitEffect(
    //             p.x + p.hitboxOffsetX + p.hitboxWidth / 2,
    //             p.y + p.hitboxOffsetY + p.hitboxHeight / 2,
    //             p.hitboxHeight
    //         );
    //     }
    // }
    
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

// rita allt varje frame
function draw() {
    ctx.drawImage(
        HPbar,
        hitcounter * HPbar.width,
        0,
        HPbar.width,
        HPbar.height,
        50,
        50,
        barWidth * barScale,
        barHeight * barScale
    );
    x = canvas.width / 2 - renderWidth / 2;
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
    // ctx.strokeStyle = "lime";
    // ctx.strokeRect(
    //     x + player.hitbox.offsetX,
    //     y + player.hitbox.offsetY,
    //     player.hitbox.width,
    //     player.hitbox.height
    // );

    
    
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
    // ctx.strokeStyle = "blue";
    // ctx.strokeRect(p.x + p.hitboxOffsetX, p.y + p.hitboxOffsetY, p.hitboxWidth, p.hitboxHeight);
}
    
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
    if (paused) {

    ctx.fillStyle = "rgba(0,0,0,0.8)";
    ctx.fillRect(0,0,canvas.width,canvas.height);

    ctx.fillStyle = "white";
    ctx.font = "40px Arial";

    ctx.fillText("Paused", canvas.width/2 - 80, 200);
    ctx.fillText("R - Restart", canvas.width/2 - 100, 290);
    ctx.fillText("ESC - Continue", canvas.width/2 - 150, 380);

}
}
// Main funktion som laddar sprites och startar gameloop
async function main() {
    
    ctx.imageSmoothingEnabled = false;
    // Ladda bakgrundslager
    const [layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8] = await Promise.all([
        loadSprite("./bg1/1.png"),
        loadSprite("./bg1/2.png"),
        loadSprite("./bg1/3.png"),
        loadSprite("./bg1/4.png"),
        loadSprite("./bg1/5.png"),
        loadSprite("./bg1/6.png"),
        loadSprite("./bg1/7.png"),
        loadSprite("./bg1/8.png")
    ]);
    // Skapa spelobjekt för varje lager
    const layer1GameObj = makeSprite(ctx, layer1, { x: 0, y: 0 }, 1);
    const layer2GameObj = makeLayer(ctx, layer2, { x: 0, y: 0 }, 1);
    const layer3GameObj = makeLayer(ctx, layer3, { x: 0, y: 0 }, 1);
    const layer4GameObj = makeLayer(ctx, layer4, { x: 0, y: 0 }, 1);
    const layer5GameObj = makeLayer(ctx, layer5, { x: 0, y: 0 }, 1);
    const layer6GameObj = makeLayer(ctx, layer6, { x: 0, y: 0 }, 1);
    const layer7GameObj = makeLayer(ctx, layer7, { x: 0, y: 0 }, 1);
    const layer8GameObj = makeLayer(ctx, layer8, { x: 0, y: 0 }, 1);
    
    let dt;
    let oldTimeStamp = 0;
    let fps;
    const debugMode = false;
    
    function gameLoop(timeStamp) {
        // Beräkna FPS, pausad, uppdatera och rita bakgrundslager
        if (!paused) {
            update();
        }
        else {
            playerMovement = 0;
            
        }
        dt = (timeStamp - oldTimeStamp) / 1000;
        oldTimeStamp = timeStamp;

        
        cameraX = worldX - canvas.width / 2;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        layer1GameObj.draw();   

        makeInfiniteScroll(dt, layer2GameObj, -playerMovement * 10);
        makeInfiniteScroll(dt, layer3GameObj, -playerMovement * 15);
        makeInfiniteScroll(dt, layer4GameObj, -playerMovement * 20);
        makeInfiniteScroll(dt, layer5GameObj, -playerMovement * 25);
        makeInfiniteScroll(dt, layer6GameObj, -playerMovement * 30);
        makeInfiniteScroll(dt, layer7GameObj, -playerMovement * 35);
        makeInfiniteScroll(dt, layer8GameObj, -playerMovement * 40);

        if (debugMode) {
            ctx.font = "128px Arial";
            ctx.fillStyle = "black";
            ctx.fillText(fps, 25, 120);
        }

        if (timeStamp - lastTimestamp > timestep) {
            frameIndex = (frameIndex + 1) % totalFrames;
            lastTimestamp = timeStamp;

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

        
        draw();

        requestAnimationFrame(gameLoop);
    }

    requestAnimationFrame(gameLoop);
}

main();