// document.addEventListener('DOMContentLoaded', function() {
//     const kelasField = document.querySelector('select[name="kelas"]');
//     const levelField = document.querySelector('select[name="level"]');
//     const hargaField = document.querySelector('input[name="harga"]');

//     // Map harga berdasarkan kelas dan level
//     const hargaMap = {
//         'Kelas Listening': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Kelas Grammar': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Kelas Writing': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Kelas Reading': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Kelas Speaking': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Business English': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Toefl Preparation': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//         'Ielts Preparation': {
//             'Beginner': 2500000,
//             'Intermediate': 300000,
//             'Advanced': 500000
//         },
//     };

//     // Fungsi untuk update harga berdasarkan pilihan kelas dan level
//     function updateHarga() {
//         const selectedKelas = kelasField.value;
//         const selectedLevel = levelField.value;

//         // Periksa apakah kombinasi kelas dan level ada di dalam map harga
//         const harga = hargaMap[selectedKelas] && hargaMap[selectedKelas][selectedLevel];

//         if (harga) {
//             hargaField.value = harga;  // Set harga di input
//         } else {
//             hargaField.value = 11;  // Set harga ke 0 jika tidak ditemukan
//         }
//     }

//     // Panggil fungsi updateHarga saat kelas atau level berubah
//     kelasField.addEventListener('change', updateHarga);
//     levelField.addEventListener('change', updateHarga);

//     // Set harga default saat halaman pertama kali dimuat
//     updateHarga();
// });
