/*function buildtower(xx) {
    manager=JSON.parse(xx);
}*/
//还是通过ajax
manager=JSON.parse(document.getElementById('towermaterial').innerHTML);
var context = document.getElementById('canvas').getContext('2d');
var canvas=document.getElementById('canvas');
var canvasoutput=document.getElementById("canvasoutput");
var contextoutput=canvasoutput.getContext('2d');
var floorManager={};
var collisionTableManager={};
var collisionTable={};
var sprites;
var gameStop=false;
var canMove=true;
var invisibleArea=[];
var spritePointer;
var characterPointer;
var enemy={};
var floorIndex=0;
var changeFloor=0;
var deletem=false;
var lastDirection={};
var from;
/*if(t.x>=1&& t.x<=8&& t.y>=1&& t.y<=4)
    invisibleArea.push(sprites.push(t)-1);
else sprites.push(t);*/

function  getPointer(xx) {
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].x*100+sprites[i].y==xx){
            spritePointer=i;
        return;}
    }
}

function renewInvisible() {
    invisibleArea.splice(0,invisibleArea.length);
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].x>=1&& sprites[i].x<=8&& sprites[i].y>=1&& sprites[i].y<=4)
            invisibleArea.push(i);}
}

function  getCharacterPointer() {
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].name=="face"){
            characterPointer=i;
            return;}
    }
}

function drawInf() {

    contextoutput.clearRect(0, 0, canvasoutput.width, canvasoutput.height);
    contextoutput.fillText( floorIndex+"th",50,30);
    contextoutput.fillText( "Level  "+sprites[characterPointer].appender.level,10,50);
    contextoutput.fillText( "Health  "+sprites[characterPointer].appender.health,10,70);
    contextoutput.fillText( "Attack  "+sprites[characterPointer].appender.attack,10,90);
    contextoutput.fillText( "Defence  "+sprites[characterPointer].appender.defence,10,110);
    contextoutput.fillText( "Gold   "+sprites[characterPointer].appender.money,10,130);
    contextoutput.fillText( "Experience  "+sprites[characterPointer].appender.experience,10,150);
    contextoutput.fillText( "Yellow Keys  "+sprites[characterPointer].appender.yk,10,170);
    contextoutput.fillText( "Blue Keys"+sprites[characterPointer].appender.bk,10,190);
    contextoutput.fillText( "Red Keys  "+sprites[characterPointer].appender.rk,10,210);
}
movetoleft={
    move:false,
    excute: function(sprite,context,time) {
        if (this.move&&canMove) {
            lastDirection=this;
            sprite.x -= 1;
            if (!(collisionTable[sprite.x*100+sprite.y] === undefined)) {
                getPointer(sprite.x*100+sprite.y);
                sprite.collision=collisionTable[sprite.x*100+sprite.y];
                sprite.x += 1;
                this.move = false;
                collisionRelfect.stop=false;
                collisionRelfect.last=time;
                  return collisionTable[Math.floor(sprite.x) + Math.floor(sprite.y)];

            }
            if (sprite.x < 0)
                sprite.x = LOGIC_W;
            this.move = false;
        }
    }
}
movetoright={
    move:false,
    excute: function(sprite,context,time) {
        if (this.move&&canMove) {
            lastDirection=this;
            sprite.x += 1;
            if (!(collisionTable[sprite.x*100+sprite.y] === undefined)) {
                getPointer(sprite.x*100+sprite.y);
                sprite.collision=collisionTable[sprite.x*100+sprite.y];
                collisionRelfect.stop=false;
                collisionRelfect.last=time;
                sprite.x -= 1;
                this.move = false;
                return collisionTable[Math.floor(sprite.x) + Math.floor(sprite.y)];
            }
            if (sprite.x>LOGIC_W)
                sprite.x = 0;
            this.move = false;
        }
    }
}
movetoup={
    move:false,
    excute: function(sprite,context,time) {
        if (this.move&&canMove) {
            lastDirection=this;
            sprite.y -= 1;
            if (!(collisionTable[sprite.x*100+sprite.y] === undefined)) {
                getPointer(sprite.x*100+sprite.y);
                sprite.collision=collisionTable[sprite.x*100+sprite.y];
                collisionRelfect.stop=false;
                collisionRelfect.last=time;
                sprite.y += 1;
                this.move = false;
                return collisionTable[Math.floor(sprite.x) + Math.floor(sprite.y)];
            }
            if (sprite.y<0)
                sprite.y = LOGIC_W;
            this.move = false;
        }
    }
}
movetodown={
    move:false,
    excute: function(sprite,context,time) {
        if (this.move&&canMove) {
            lastDirection=this;
            sprite.y += 1;
            if (!(collisionTable[sprite.x*100+sprite.y] === undefined)) {
                getPointer(sprite.x*100+sprite.y);
                sprite.collision=collisionTable[sprite.x*100+sprite.y];
                sprite.y -= 1;
                this.move = false;
                collisionRelfect.stop=false;
                collisionRelfect.last=time;
                return collisionTable[Math.floor(sprite.x) + Math.floor(sprite.y)];
            }
            if (sprite.y>=LOGIC_W)
                sprite.y = 0;
            this.move = false;
        }
    }
}
///////////////////////////////////////////////////////////////////////////////////////////

collisionRelfect={
    last:0,
    stop:true,
    firstCollision:true,
    excute: function(sprite,context,time) {
        if(sprite.collision!=undefined )
        {
            if(sprite.collision==5){
                from='item6';
                changeFloor=1;
                sprite.collision=undefined;
                canMove=true;
                return;
            }
            else if(sprite.collision==6){
                from='item5';
                changeFloor=-1;
                sprite.collision=undefined;
                canMove=true;
                return;
            }
            else if(sprite.collision==77){
                sprite.collision=undefined;
                lastDirection.move=true;
                canMove=true;
                sprites[characterPointer].appender.yk+=1;
                deletem = true;
                return;
            }
            else if(sprite.collision==78){
                sprite.collision=undefined;
                lastDirection.move=true;
                canMove=true;
                sprites[characterPointer].appender.bk+=1;
                deletem = true;
                return;
            }
            else if(sprite.collision==79){
                sprite.collision=undefined;
                lastDirection.move=true;
                canMove=true;
                sprites[characterPointer].appender.rk+=1;
                deletem = true;
                return;
            }
            else if(sprite.collision==57){
                sprite.collision=undefined;
                canMove=true;
               if(sprites[characterPointer].appender.yk>0){
                   sprites[characterPointer].appender.yk-=1;
                lastDirection.move=true;
                deletem = true;}
                return;
            }

            else if(sprite.collision==58){
                sprite.collision=undefined;
                canMove=true;
                if(sprites[characterPointer].appender.bk>0){
                    sprites[characterPointer].appender.bk-=1;
                    lastDirection.move=true;
                    deletem = true;}
                return;
            }

            else if(sprite.collision==59){
                sprite.collision=undefined;
                canMove=true;
                if(sprites[characterPointer].appender.rk>0){
                    sprites[characterPointer].appender.rk-=1;
                    lastDirection.move=true;
                    deletem = true;}
                return;
            }
            else if((sprite.collision>=81&&sprite.collision<=84)||(sprite.collision>=89&&sprite.collision<=91)||
                (sprite.collision>=93&&sprite.collision<=95)||(sprite.collision>=97&&sprite.collision<=98)||
                (sprite.collision>=101&&sprite.collision<=102)||(sprite.collision>=105&&sprite.collision<=106)||
                (sprite.collision>=109&&sprite.collision<=110)||(sprite.collision>=113&&sprite.collision<=120)
                ){
                var t=getMonsterInf(sprite.collision);
                for(sp in t )
                    enemy[sp]=t[sp];
                sprite.collision=undefined;
                canMove=true;
                sprites[characterPointer].appender.health+=enemy.h;
                sprites[characterPointer].appender.money+=enemy.g;
                sprites[characterPointer].appender.attack+=enemy.a;
                sprites[characterPointer].appender.defence+=enemy.d;
                sprites[characterPointer].appender.experience+=enemy.e;
                lastDirection.move=true;
                deletem = true;
                return;
            }
            else if(sprite.collision<9||sprite.collision>53){
               sprite.collision=undefined;
                canMove=true;
                return;
            }
            if(this.firstCollision){
                var t=getMonsterInf(sprite.collision);
             for(sp in t )
             enemy[sp]=t[sp];//因为我比较烦，所以先不写胜利
            context.save();
            context.fillStyle="#00FFFF";//颜色到时再说
            context.font="12px Georgia";
            var ns={};
            for(var sp in  sprites[spritePointer])
                ns[sp]=sprites[spritePointer][sp];
            ns.x=8;
            ns.y=2.5;
            sprites.push(ns);
            var test1=new Sprite("face1",new spriteSheetPainter(img1,facecells),
                [new changeface(200)]);
            test1.x=3;
            test1.y=2.5;
           sprites.push(test1);
            this.firstCollision=false;
            for(var i=0;i<invisibleArea.length;i++){
            sprites[invisibleArea[i]].visible=false; }  //changeface 在前?
            canMove=false;
        }

            {
                context.fillRect(trans(1), trans(1), trans(11), trans(4));
                context.save();
                context.fillStyle = "#000000";
                context.fillText("Health  " + sprites[characterPointer].appender.health, trans(3), 55);
                context.fillText("Attack  " + sprites[characterPointer].appender.attack, trans(3), 75);
                context.fillText("Defence  " + sprites[characterPointer].appender.defence, trans(3), 95);
                context.fillText("Health  " + enemy.h, trans(8), 55);
                context.fillText("Attack  " + enemy.a, trans(8), 75);
                context.fillText("Defence  " + enemy.d, trans(8), 95);
                context.fillText("Experience  " + sprites[characterPointer].appender.experience, trans(3), 165);
                context.fillText("Gold  " + sprites[characterPointer].appender.money, trans(3), 185);
                context.fillText("Experience  " + enemy.e, trans(8), 165);
                context.fillText("Gold  " + enemy.g, trans(8), 185);
                context.restore();
                if (time - this.last > 70){

                    this.last=time;
                    var cs = sprites[characterPointer].appender.defence - enemy.a * (1 + Math.random());
                cs = Math.floor(cs);
                if (cs > 0) cs = 0;
                sprites[characterPointer].appender.health += cs;
                    if (sprites[characterPointer].appender.health <=0)sprites[characterPointer].appender.health=0;
                var ss = enemy.d - sprites[characterPointer].appender.attack * (1 + Math.random());
                ss = Math.floor(ss);
                if (ss > 0) ss = 0;
                enemy.h += ss;
                    if(enemy.h<0)enemy.h=0;
                //////////////////////////////////////
                if (enemy.h <= 0) {
                    this.stop = true;
                    deletem = true;
                    //alert("l");
                }
                 if (sprites[characterPointer].appender.health <= 0) {
                     context.fillRect(trans(1), trans(1), trans(11), trans(4));
                     context.fillStyle = "#000000";
                     context.font="40px Arial";
                     context.fillText("Lost", trans(5),100);
                     contextoutput.clearRect(0,0,canvasoutput.width,canvasoutput.height);
                     contextoutput.font="40px Arial";
                     contextoutput.fillText("Lost",20,100);
                        alert("Unfortunately you lost");
                        cancelRequestAnimationFrame(handle);
                    }
            }
            }
           if(this.stop){
               context.restore();
                sprites.pop();
                sprites.pop();
               sprites[characterPointer].appender.experience+=enemy.e;
               sprites[characterPointer].appender.money+=enemy.g;
                this.last=time;
                sprite.collision=undefined
                for(var i=0;i<invisibleArea.length;i++){
                    sprites[invisibleArea[i]].visible=true; }
                canMove=true;
                this.firstCollision=true;
            }
        }
    }
}
document.onkeydown=function(event){
    var event=event||window.event;
    if(!gameStop) {
        if (event.keyCode == 65) {
            movetoleft.move = true;
        }
        if (event.keyCode == 87) {
            movetoup.move = true;
        }
        if (event.keyCode == 83) {
            movetodown.move = true;
        }
        if (event.keyCode == 68) {
            movetoright.move = true;
        }
    }
}
window.onload= function () {
   for (var sp in manager) {
       if(sp!='cm'){
       var t=[],fl=manager[sp];
        for(var j=0;j<fl.length;j++){
           var  test=new Sprite(fl[j].name, new spriteSheetPainter(img2,fl[j].painter.cells),[new changeface(300)]);
            test.x=fl[j].x;
            test.y=fl[j].y;
            t.push(test);
        }
        floorManager[sp]=t;}
       else{
           for(var clt in manager[sp]){
           var test=manager[sp][clt];
           collisionTableManager[clt]={};
            var b= collisionTableManager[clt];
               for(ct in test){
                   b[ct]=test[ct];
               }
           }
   // alert("finish");

       }

    }
    sprites =floorManager['0'];
    collisionTable=collisionTableManager['0'];
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].x>=1&& sprites[i].x<=8&& sprites[i].y>=1&& sprites[i].y<=4)
            invisibleArea.push(i);
        if(sprites[i].name=='item6')
        {
            var test1=new Sprite("face",new spriteSheetPainter(img1,facecells),
                [movetoleft,new changeface(200),movetodown,movetoright,movetoup,collisionRelfect],
                new monsterInf(0,2000,5,5,0,0));
            test1.x=sprites[i].x;
            test1.y=sprites[i].y;
      characterPointer =sprites.push(test1)-1;
        }
    }
    contextoutput.font="12px Georgia";
    handle=window.requestAnimationFrame(p);
}
function p(time) {
    //alert("jojojo");
    //context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img3,0,0);
    drawInf();
    for (var i = 0; i < sprites.length; i++) {
        sprites[i].paint(context);
        sprites[i].update(context, time);
    }
    if(deletem){
        deletem=false;
        collisionTable[sprites[spritePointer].x * 100 + sprites[spritePointer].y] = undefined;
        sprites.splice(spritePointer,1);
        getCharacterPointer();
        renewInvisible();
    }
    if(changeFloor!=0){
        if(floorManager[floorIndex+changeFloor]!=undefined){
            floorIndex+=changeFloor;
            getCharacterPointer();
            var t=new Sprite("face",new spriteSheetPainter(img1,facecells),
                [movetoleft,new changeface(200),movetodown,movetoright,movetoup,collisionRelfect],
                new monsterInf(0,2000,20,20,20,20));
            for(sp in sprites[characterPointer].appender){
                t.appender[sp]=sprites[characterPointer].appender[sp];
            }
            sprites.splice(characterPointer,1);
            sprites=floorManager[floorIndex];
            for(var i=0;i<sprites.length;i++){
                if(sprites[i].name==from){//等会再搞那个细节
                    t.x=sprites[i].x;
                    t.y=sprites[i].y;
                }
            }
            sprites.push(t);
            collisionTable=collisionTableManager[floorIndex];
            renewInvisible();
            getCharacterPointer();
        }
        changeFloor=0;
    }
    if (!gameStop)
        handle = window.requestAnimationFrame(p);
    else {
        window.cancelRequestAnimationFrame(handle);
    }
}