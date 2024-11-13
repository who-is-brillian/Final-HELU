$(document).ready(function () {
    // When the page is fully loaded, trigger the bounce animation
    $('.navbar').addClass('bounce');
  });


    //Counter Students
    $(document).ready(function(){
        let targetCount = parseInt($('#counter1').data('target')); // Ambil nilai target dari data-target
        $({ countNum: $('#counter1').text() }).animate({ countNum: targetCount }, {
          duration: 2000,
          easing: 'linear',
          step: function() {
            $('#counter1').text(Math.floor(this.countNum));
          },
          complete: function() {
            $('#counter1').text(targetCount);
          }
        });
      });
      
    
    //Counter Mentor

    $(document).ready(function(){
        let targetCount = parseInt($('#counter2').data('target')); // Ambil nilai target dari data-target
        $({ countNum: $('#counter2').text() }).animate({ countNum: targetCount }, {
          duration: 2000,
          easing: 'linear',
          step: function() {
            $('#counter2').text(Math.floor(this.countNum));
          },
          complete: function() {
            $('#counter2').text(targetCount);
          }
        });
      });

  //Counter Class
  $(document).ready(function(){
    let targetCount = parseInt($('#counter3').data('target')); // Ambil nilai target dari data-target
    $({ countNum: $('#counter3').text() }).animate({ countNum: targetCount }, {
      duration: 2000,
      easing: 'linear',
      step: function() {
        $('#counter3').text(Math.floor(this.countNum));
      },
      complete: function() {
        $('#counter3').text(targetCount);
      }
    });
  });

// Set waktu hitung mundur (contoh: 24 jam = 86400 detik)
let duration = 86400; // 24 jam dalam detik

let countdownTimer = setInterval(function() {
  // Hitung jam, menit, dan detik dari durasi
  let hours = Math.floor(duration / 3600); // Hitung jam
  let minutes = Math.floor((duration % 3600) / 60); // Hitung menit
  let seconds = duration % 60; // Hitung detik

  // Format jam, menit, dan detik agar selalu tampil 2 digit
  hours = hours < 10 ? "0" + hours : hours;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  seconds = seconds < 10 ? "0" + seconds : seconds;

  // Tampilkan hasil dalam format 24h 60m 60s
  $("#countdown").text(hours + "h " + minutes + "m " + seconds + "s");

  // Jika durasi habis, hentikan timer
  if (duration <= 0) {
    clearInterval(countdownTimer);
    $("#countdown").text("EXPIRED");
  }

  duration--; // Kurangi waktu setiap detik
}, 1000);
