
//Button SignIn SignUp Navigasi Bar
$(".btn-signIn").hover(
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#d8c4b6'); // saat mouse masuk
  },
  function() {
    $(this).css('background-color', '#f5efe7');
    $(this).css('color', '#213555'); // saat mouse keluar (reset ke warna asli)
  }
); 

$(".btn-signUp").hover(
  function() {
    $(this).css('background-color', '#f5efe7');
    $(this).css('color', '#213555'); // saat mouse masuk
  },
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#d8c4b6'); // saat mouse keluar (reset ke warna asli)
  }
);

//button info selengkapnya
$(".btn-class-info").hover(
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#f5efe7'); // saat mouse masuk
  },
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#f5efe7'); // saat mouse keluar (reset ke warna asli)
  }
);

//button price
$(".btn-price1").hover(
  function() {
    $(this).css('background-color', '#7c93c3');
    $(this).css('color', '#f5efe7'); // saat mouse masuk
    $(this).css('scale', '1.05')
    $(this).css('transition','0.5s')
  },
  function() {
    $(this).css('background-color', '#7c93c3');
    $(this).css('color', '#f5efe7'); // saat mouse keluar (reset ke warna asli)
    $(this).css('scale', '1')
  }
);
$(".btn-price2").hover(
  function() {
    $(this).css('background-color', '#4f709c');
    $(this).css('color', '#f5efe7'); // saat mouse masuk
    $(this).css('scale', '1.05')
    $(this).css('transition','0.5s')

  },
  function() {
    $(this).css('background-color', '#4f709c');
    $(this).css('color', '#f5efe7'); // saat mouse keluar (reset ke warna asli)
    $(this).css('scale', '1')
  }
);
$(".btn-price3").hover(
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#f5efe7'); // saat mouse masuk
    $(this).css('scale', '1.05')
    $(this).css('transition','0.5s')
  },
  function() {
    $(this).css('background-color', '#213555');
    $(this).css('color', '#f5efe7'); // saat mouse keluar (reset ke warna asli)
    $(this).css('scale', '1')
  }
);


//Button Daftar sekarang
$(".btn-daftar").hover(
function() {
  $(this).css('background-color', '#DFF5FF');
  $(this).css('color', '#213555'); // saat mouse masuk
},
function() {
  $(this).css('background-color', '#f5efe7');
  $(this).css('color', '#213555'); // saat mouse keluar (reset ke warna asli)
}
);

//animasi shake diskon
$(document).ready(function(){
  function shake() {
    $('#limited-offer').animate({marginLeft: "-10px"}, 100)
                       .animate({marginLeft: "10px"}, 100)
                       .animate({marginLeft: "-10px"}, 100)
                       .animate({marginLeft: "10px"}, 100)
                       .animate({marginLeft: "0px"}, 100); // Return to original position
  }

  // Trigger the animation when the page loads
  setInterval(shake, 500); // Shake every second
});

// typing effect
$(document).ready(function() {
  var texts = [
    "WHO WE ARE AND WHY WE DO WHAT WE DO?",
    "WE ARE PASSIONATE ABOUT CREATING IMPACTFUL EXPERIENCES.",
    "FEEL FREE TO REACH OUT FOR ANY PROJECT INQUIRIES."
  ];

  // Fungsi untuk membuat efek mengetik
  function typeEffect(element, text, index = 0) {
    if (index < text.length) {
      element.append(text[index]); // Tambahkan karakter satu per satu
      setTimeout(function() {
        typeEffect(element, text, index + 1); // Lanjutkan mengetik
      }, 80); // Kecepatan mengetik (100ms per huruf)
    }
  }

  // Panggil efek mengetik untuk setiap elemen
  typeEffect($('.typing-effect1'), texts[0]);
    typeEffect($('.typing-effect2'), texts[1]);
    typeEffect($('.typing-effect3'), texts[2]);
});