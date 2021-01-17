from PIL import Image

MAX_NILAI_WARNA = 256;
MAX_NILAI_BIT = 8;

def jadikan_image(data, resolution):
    image = Image.new("RGB", resolution);
    image.putdata(data);

    return image;


def hapus_n_LSB_pada_mediasembunyi(value, n):
    value = value >> n;
    return value << n;


def ambil_n_MSB_pada_gambarsembunyi(value, n):
    return value >> MAX_NILAI_BIT - n;


def enkripsi(gambar_yang_disembunyikan, media_sembunyi, n_bits):
    lebar, tinggi = gambar_yang_disembunyikan.size;

    gambar_sembunyi = gambar_yang_disembunyikan.load();
    medium_sembunyi = media_sembunyi.load();

    data = [];

    for y in range(tinggi):
        for x in range(lebar):
            
            #menyalin MSB dari gambar_sembunyi
            sisipanMSB_r, sisipanMSB_g, sisipanMSB_b = gambar_sembunyi[x,y];
            sisipanMSB_r = ambil_n_MSB_pada_gambarsembunyi(sisipanMSB_r, n_bits);
            sisipanMSB_g = ambil_n_MSB_pada_gambarsembunyi(sisipanMSB_g, n_bits);
            sisipanMSB_b = ambil_n_MSB_pada_gambarsembunyi(sisipanMSB_b, n_bits);

            #menghapus LSB dari medium_sembunyi
            sisipanLSB_r, sisipanLSB_g, sisipanLSB_b = medium_sembunyi[x,y];
            sisipanLSB_r = hapus_n_LSB_pada_mediasembunyi(sisipanLSB_r, n_bits);
            sisipanLSB_g = hapus_n_LSB_pada_mediasembunyi(sisipanLSB_g, n_bits);
            sisipanLSB_b = hapus_n_LSB_pada_mediasembunyi(sisipanLSB_b, n_bits);

            #menjumlahkan hasil biner baru gambar_sembunyi dan medium_sembunyi
            #dan memasukkannya ke dalam array data
            data.append((
                sisipanMSB_r + sisipanLSB_r,
                sisipanMSB_g + sisipanLSB_g,
                sisipanMSB_b + sisipanLSB_b
            ));

    return jadikan_image(data, gambar_yang_disembunyikan.size);


if "__main__":
    print ("Ketik nama gambar yang akan di-enkripsi : "); 
    input_gambar1 = input();

    print ("Ketik nama gambar yang menjadi media enkripsi : "); 
    input_gambar2 = input();

    print ("Ketik nama gambar hasil enkripsi : ");
    output_gambar = input();

    lokasi_gambar_yang_disembunyikan = "./input/"+ input_gambar1 +".tiff";
    lokasi_media_sembunyi = "./input/"+ input_gambar2 +".tiff";
    lokasi_gambar_terenkripsi = "./output/"+ output_gambar +".tiff";
    
    n_bits = 3;

    gambar_yang_disembunyikan = Image.open(lokasi_gambar_yang_disembunyikan);
    media_sembunyi = Image.open(lokasi_media_sembunyi);
    enkripsi(gambar_yang_disembunyikan, media_sembunyi, n_bits).save(lokasi_gambar_terenkripsi);
    
