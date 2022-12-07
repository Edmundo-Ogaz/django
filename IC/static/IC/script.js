
    // if there's a cookie with the name myClock, use that value as the deadline
    //if(document.cookie && document.cookie.match('myClock')){
      // get deadline value from cookie
      //var deadline = document.cookie.match(/(^|;)myClock=([^;]+)/)[2];
    //}

    // otherwise, set a deadline 10 minutes from now and
    // save it in a cookie with that name
    //else{
      // create deadline 10 minutes from now
const timeInMinutes = 8;
const currentTime = Date.parse(new Date());
const deadline = new Date(currentTime + timeInMinutes * 60 * 1000);
let minutesSpan;
let secondsSpan;
let action = false;

// store deadline in cookie for future reference
      //document.cookie = 'myClock=' + deadline + '; path=/; http://localhost/Codeigniter';
    //}


    initializeClock('clock', deadline);

    function getTimeRemaining(endtime){
        const t = Date.parse(endtime) - Date.parse(new Date());
        const seconds = Math.floor((t / 1000) % 60);
        const minutes = Math.floor((t / 1000 / 60) % 60);
        return {
            'total': t,
            'minutes': minutes,
            'seconds': seconds
        };
    }

    function initializeClock(id, endtime){
        const clock = document.getElementById(id);

        minutesSpan = clock.querySelector('.minutes');
        secondsSpan = clock.querySelector('.seconds');
    }

    const timeinterval = setInterval(updateClock,1000);

 // run function once at first to avoid delay
let flag;

let flag_o;

function updateClock(){
    const timeAlert = document.getElementById("time_alert");
    const t = getTimeRemaining(deadline);
    minutesSpan.innerHTML = t.minutes;
        secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);
        //console.log(t);
        if(t.minutes<=1 && !flag && !flag_o){
            flag = true;
        }
        if(flag && !flag_o){
            timeAlert.style.display = "block";
            flag = false;
            flag_o = true;
        }
        if(!flag && flag_o && t.minutes<=0){
            timeAlert.style.display = "none";
            document.getElementById("clock").style.backgroundColor = 'red';
            document.getElementById("clock").style.color = 'white';
            flag = true;
            flag_o = true;
        }

        if(t.total<=0){
            action=true;
            clearInterval(timeinterval);
            document.getElementById("myForm").submit();// Form submission
        }
    }

    updateClock();
flag = false;
flag_o = false;

function checker(){
    //let bin = "000000000000000000000000000000000000000000000000000000000000000000000000000".split("");
    const check = document.getElementsByName("check[]");
    const checkArray = Array.from(check);
    let index;
    let bin = Array();
    for (let i = 0; i < 75; i++) {
        index = (i % 3) * 25 + Math.floor(i / 3);
        bin[index] = checkArray[i].checked ? '1' : '0';
    }
    bin = bin.join('');
    return bin;
}
$(window).bind('beforeunload', function(){
            if(!action){
                bin=checker()
                console.log(navigator.sendBeacon("http://localhost/Codeigniter/index.php/Pruebas/test_ic/beacon?bin=beacon".concat(bin).concat("&status=finished")));
                return 'Are you sure you want to leave?';
            }
        });
        document.getElementById("submiter").onclick = function(){
            console.log(checker());
        };
