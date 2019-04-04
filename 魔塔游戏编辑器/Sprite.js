/**
 * Created by DD on 2015/11/7.
 */
/**
 * Created by DD on 2015/11/7.
 */

var context = document.getElementById('canvas').getContext('2d');
var contextinput = document.getElementById('canvasinput').getContext('2d');
var canvas=document.getElementById('canvas');
var canvasinput=document.getElementById('canvasinput');
var canvasoutput=document.getElementById("canvasoutput");
var contextoutput=canvasoutput.getContext('2d');
var canvaskit=document.getElementById("canvaskit");
var contextkit=canvaskit.getContext('2d');
var canMove=true;
var dragging=false;

///////////////////////////////////////////////////////////////////////////         中间的一定要变


////////////////////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////             中间的一定要变

//查js new
//查js的底层实现
function windowToCanvas(x, y) {
    var bbox = canvas.getBoundingClientRect();

    return { x: x - bbox.left * (canvas.width  / bbox.width),
        y: y - bbox.top  * (canvas.height / bbox.height)
    };
}
function windowToCanvasinput(x, y) {
    var bbox = canvasinput.getBoundingClientRect();

    return { x: x - bbox.left * (canvasinput.width  / bbox.width),
        y: y - bbox.top  * (canvasinput.height / bbox.height)
    };
}

function windowToCanvaskit(x, y) {
    var bbox = canvaskit.getBoundingClientRect();

    return { x: x - bbox.left * (canvaskit.width  / bbox.width),
        y: y - bbox.top  * (canvaskit.height / bbox.height)
    };
}
//这个细节到时候再说

var inputItemTable={};

function deleteSByLoc(loc) {
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].x== loc.x&&sprites[i].y==loc.y ){
           // alert("hahahaha fd");
            sprites.splice(i,1);
            //alert("ri le gou ");
            return;
        }
    }
}

function transparentSByLoc(loc) {
    for(var i=0;i<sprites.length;i++){
        if(sprites[i].x== loc.x&&sprites[i].y==loc.y ){
            sprites[i].width=sprites[i].height=0.5;
            return;
        }
    }
}
/***********************************above  sprite constructor ********************************************************/
function drawGrid(color) {
    context.save()
    context.strokeStyle = color;
    context.lineWidth = 0.5;

    context.drawImage(img3,0,0);
    for (var i = 0; i < context.canvas.width; i += UNIT_LENGTH) {
        context.beginPath();
        context.moveTo(i, 0);
        context.lineTo(i, context.canvas.height);
        context.stroke();
    }
    for (var i = 0; i < context.canvas.height; i +=UNIT_LENGTH) {
        context.beginPath();
        context.moveTo(0, i);
        context.lineTo(context.canvas.width, i);
        context.stroke();
    }
    context.restore();
}
/*************************************************back ground********************************************************/

//var timer= new animationTimer(60);
var insertname={}//and id
insertname.id=0;
insertname.loc=0;
insertname.name='item0';


///////////////////////
function paintmonster() {
    contextinput.clearRect(0, 0,canvasinput.width,canvasinput.height);
    input.painter.index=inputmonsterfloor;
    input.x=0;
    var cid=-2;
    var ic=getLoc(10);
    for(var i=0;i<ic;i++){
        if(cid!=inputcells[input.painter.index].id){
            cid=inputcells[input.painter.index].id
            input.paint(contextinput);
            input.x++;
        }
        input.painter.advance();
    }
}
var inputmonsterfloor=0;
var floorindex=0;
var floormagent={};
floormagent[floorindex]=[];
floormagent['cm']={};
var collisionTableManager=floormagent['cm'];
collisionTableManager[floorindex]={};
var collisionTable=collisionTableManager[floorindex];
var sprites=floormagent[floorindex];
var input=new Sprite("screeninput",new spriteSheetPainter(img2,inputcells));
//var test=new Sprite("face",new spriteSheetPainter(img1,facecells),[movetoleft,new changeface(200),movetodown,movetoright,movetoup]);
//sprites.push(test);
/*var test=new Sprite("face",new spriteSheetPainter(img1,facecells),
    [movetoleft,new changeface(200),movetodown,movetoright,movetoup,collisionRelfect],
    new monsterInf(0,1000,10,10,0,0));*/
//var animal=document.getElementById("animal");
var nextmF=document.getElementById("nextmonster");
var lastmF=document.getElementById("lastmonster");
var nextfloor=document.getElementById("nextfloor");
var lastfloor=document.getElementById("lastfloor");
var submit=document.getElementById("submit");
var judgestart=false;
//sprites.push(test);
window.onload= function () {
    eraser=new Sprite("eraser",new imgpainter("eraser.jpg"));
    eraser.x=0;
    eraser.y=0;
    eraser.width=eraser.height=2;
    drop=new Sprite("drop",new imgpainter("drop.png"));
    drop.x=0;
    drop.y=3;
    drop.width=drop.height=2;
    handle=window.requestAnimationFrame(p);
}
function p(time) {
    context.clearRect(0,0,canvas.width,canvas.height);
    contextoutput.clearRect(0, 0,100,20);
    contextoutput.fillText( "floor:  "+floorindex,10,10);
    drawGrid('lightgray');
    for(var i=0;i<sprites.length;i++){
   sprites[i].paint(context);
   sprites[i].update(context,time);}
   eraser.paint(contextkit);
   drop.paint(contextkit);
   paintmonster();
    handle=window.requestAnimationFrame(p);
}


canvasinput.onmousedown= function (e) {
    if(!judgestart){
        var loc=windowToCanvasinput(e.clientX,e.clientY);
        var t={};
        t.x=Math.floor(loc.x/UNIT_LENGTH);
        t.y=Math.floor( loc.y/UNIT_LENGTH);
        var i=getLoc(t.x);
        insertname.id=inputcells[i+inputmonsterfloor].id;
        insertname.name="item"+ insertname.id;
        insertname.loc=i+inputmonsterfloor;
        contextoutput.font="12px Georgia";
        contextoutput.clearRect(0, 0, canvasoutput.width, canvasoutput.height);
        var inf=getMonsterInf(insertname.id);
        if(inf!=undefined){
            contextoutput.fillText( "health:  "+inf.h,10,50);
            contextoutput.fillText( "attack  "+inf.a,10,70);
            contextoutput.fillText( "defence  "+inf.d,10,90);
            contextoutput.fillText( "experience  "+inf.e,10,110);
            contextoutput.fillText( "money  "+inf.g,10,130);
        }
        var cell=inputcells[insertname.loc];
        contextoutput.drawImage(img2,cell.x,cell.y,cell.w,cell.h,20,150,80,80);
    }
}
canvaskit.onmousedown= function (e) {
    var loc=windowToCanvaskit(e.clientX,e.clientY);
    var t={};
    t.x=Math.floor(loc.x/UNIT_LENGTH);
    t.y=Math.floor( loc.y/UNIT_LENGTH);
    if(t.x>=eraser.x&& t.x<eraser.x+eraser.width&& t.y>=eraser.y&& t.y<eraser.y+eraser.height){
        insertname.name="eraser";
        insertname.id=-1;
        insertname.loc=-1;
       // alert("get eraser");
        //alert(sprites.length);
        contextoutput.clearRect(0, 0,canvasoutput.width,canvasoutput.height);
        eraser.paint(contextoutput);

    }
    if(t.x>=drop.x&& t.x<drop.x+drop.width&& t.y>=drop.y&& t.y<drop.y+drop.height){
        insertname.name="drop";
        insertname.id=-2;
        insertname.loc=-2;
        contextoutput.clearRect(0, 0,canvasoutput.width,canvasoutput.height);
        drop.paint(contextoutput);
        //alert("get drop");
    }
}


canvas.onmousedown= function (e) {
    dragging=true;
   //alert(insertname.id);
    if(insertname.id==-2){
        var t={};
        var loc = windowToCanvas(e.clientX, e.clientY);
        t.x = Math.floor(loc.x / UNIT_LENGTH);
        t.y = Math.floor(loc.y / UNIT_LENGTH);
        collisionTable[t.x * 100 + t.y] =undefined;
        transparentSByLoc(t);
        dragging=false;
        return;
    }
    if(insertname.id==-1){
       // alert("hhhh");
        var loc = windowToCanvas(e.clientX, e.clientY);
        var t={};
        //alert("i'd like it");
        t.x = Math.floor(loc.x / UNIT_LENGTH);
        t.y = Math.floor(loc.y / UNIT_LENGTH);
        collisionTable[t.x * 100 + t.y] =undefined;
        //alert("ri");
        deleteSByLoc(t);
        //alert("feww");
        dragging=false;
        return;
    }
        if (inputItemTable[insertname.name] == undefined) {
            var celll = [];
            celll.push(inputcells[insertname.loc]);
            if(insertname.loc + 1<inputcells.length&&inputcells[insertname.loc + 1].id==inputcells[insertname.loc].id)
            celll.push(inputcells[insertname.loc + 1]);
            if(insertname.loc + 2<inputcells.length&&inputcells[insertname.loc + 2].id==inputcells[insertname.loc].id)
            celll.push(inputcells[insertname.loc + 2]);
            if(insertname.loc + 3<inputcells.length&&inputcells[insertname.loc + 3].id==inputcells[insertname.loc].id)
            celll.push(inputcells[insertname.loc + 3]);
            inputItemTable[insertname.name] = celll;
        }

        if(insertname.id==5){
            dragging=false;
            for(sp in collisionTable){
                if(collisionTable[sp]==5){
                    alert("只能有一个上升梯子");
                return;}
            }
        }
        if(insertname.id==6){
            dragging=false;
            for(sp in collisionTable){
                if(collisionTable[sp]==6){
                    alert("只能有一个下降梯子");
                return;}
            }
        }
    var t = new Sprite(insertname.name, new spriteSheetPainter(img2, inputItemTable[insertname.name]),[new changeface(300)]);
    var loc = windowToCanvas(e.clientX, e.clientY);
    t.x = Math.floor(loc.x / UNIT_LENGTH);
    t.y = Math.floor(loc.y / UNIT_LENGTH);
    collisionTable[t.x * 100 + t.y] = insertname.id;//1 represent enemy
    deleteSByLoc(t);
    sprites.push(t);
}
canvas.onmousemove= function (e) {
    if(dragging){
    var t ={};
    var loc = windowToCanvas(e.clientX, e.clientY);
    t.x = Math.floor(loc.x / UNIT_LENGTH);
    t.y = Math.floor(loc.y / UNIT_LENGTH);
     if( collisionTable[t.x * 100 + t.y]==undefined){
     deleteSByLoc(t);
     var tt= new Sprite(insertname.name, new spriteSheetPainter(img2, inputItemTable[insertname.name]),[new changeface(300)]);
     tt.x= t.x;
     tt.y= t.y;
    collisionTable[t.x * 100 + t.y] = insertname.id;//1 represent enemy
    sprites.push(tt);}
    }
}

document.onmouseup= function (e) {
    dragging=false;
}
function getLoc (xx) {
    var i= 0,cc= 0,id=inputcells[inputmonsterfloor].id;
    if(inputmonsterfloor>=inputcells.length-1) return 0;
    while(cc!=xx&&inputmonsterfloor+i<inputcells.length){
        if(inputcells[inputmonsterfloor+i].id!=id)
        {id=inputcells[inputmonsterfloor+i].id;
            cc++;
        }
        i++;
    }
    if(i!=0)
    return i-1;
    return 0;
}
/*animal.onclick= function () {
    if(!judgestart){
    animal.setAttribute("value","stop");
    judgestart=true;
}
    else{
        animal.setAttribute("value","animation");
        judgestart=false;
    }
    animal.blur();
}*/
var scrollmfloor=[];
nextmF.onclick= function () {
    var test=getLoc(10);
    if(inputmonsterfloor+test<inputcells.length-1){
    scrollmfloor.push(test);
    inputmonsterfloor+=test;}
}

lastmF.onclick= function () {
    inputmonsterfloor-=scrollmfloor.pop();
    if(inputmonsterfloor==0) scrollmfloor.push(0);
}

nextfloor.onclick= function () {
  floorindex+=1;
    if(floormagent[floorindex]==undefined){
        floormagent[floorindex]=[];
        collisionTableManager[floorindex]={};
    }
    sprites= floormagent[floorindex];
    collisionTable= collisionTableManager[floorindex];
}

lastfloor.onclick= function () {
    floorindex-=1;
    if(floormagent[floorindex]==undefined){
        floormagent[floorindex]=[];
        collisionTableManager[floorindex]={};
    }
    sprites= floormagent[floorindex];
    collisionTable= collisionTableManager[floorindex];
}

function registrationProcessed() {
    if (request.readyState == 4) {
        if (request.status == 200) {
            submit.disabled=true;
            document.getElementById("testjson").innerHTML =
                request.responseText;
        }
    }
}
submit.onclick= function () {
     var  image = canvas.toDataURL();
    var t=[];
    t=floormagent['0'];
    var tes=false;
    for(var i=0;i< t.length;i++){
        if(t[i].name=='item6')
        tes=true;
    }
    if(!tes){
        alert("矮油，骚年，0层没有楼梯如何召唤主角");
        return 0;
    }
    var name=document.getElementById("name").innerHTML;
    var submission=JSON.stringify(floormagent);
    request = createRequest();
    var url = "answer.php";
    var requestData = "username=" +
        decodeURI(name)+ "&image="+decodeURI(image)+"&tower=" +
        decodeURI(submission);
    request.onreadystatechange = registrationProcessed;
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type",
        "application/x-www-form-urlencoded");
    request.send(requestData);
}

