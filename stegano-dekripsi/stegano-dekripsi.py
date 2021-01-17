from PIL import Image

MAX_NILAI_WARNA = 256;
MAX_NILAI_BIT = 8;

def jadikan_image(data, resolution):
    image = Image.new("RGB", resolution);
    image.putdata(data);

    return image;


def ambil_n_LSB_pada_gambarterenkripsi(value, n):
    value = value << MAX_NILAI_BIT - n;
    value = value % MAX_NILAI_WARNA;
    return value >> MAX_NILAI_BIT - n;


def geserkiri_n_bits_sebanyak_8(value, n):
    return value << MAX_NILAI_BIT - n;


def dekripsi(gambar_yang_didekripsi, n_bits):
    lebar, tinggi = gambar_yang_didekripsi.size;
    gambar_enkripsi = gambar_yang_didekripsi.load();

    data = [];

    for y in range(tinggi):
        for x in range(lebar):

            LSBterenkripsi_r, LSBterenkripsi_g, LSBterenkripsi_b = gambar_enkripsi[x,y];

            LSBterenkripsi_r = ambil_n_LSB_pada_gambarterenkripsi(LSBterenkripsi_r, n_bits);
            LSBterenkripsi_g = ambil_n_LSB_pada_gambarterenkripsi(LSBterenkripsi_g, n_bits);
            LSBterenkripsi_b = ambil_n_LSB_pada_gambarterenkripsi(LSBterenkripsi_b, n_bits);

            LSBterenkripsi_r = geserkiri_n_bits_sebanyak_8(LSBterenkripsi_r, n_bits);
            LSBterenkripsi_g = geserkiri_n_bits_sebanyak_8(LSBterenkripsi_g, n_bits);
            LSBterenkripsi_b = geserkiri_n_bits_sebanyak_8(LSBterenkripsi_b, n_bits);

            data.append((
                LSBterenkripsi_r,
                LSBterenkripsi_g,
                LSBterenkripsi_b
            ));

    return jadikan_image(data, gambar_yang_didekripsi.size);


if "__main__":
    print ("Ketik nama gambar yang akan di-dekripsi : "); 
    input_gambar = input();

    print ("Ketik nama gambar hasil dekripsi : ");
    output_gambar = input();
    
    lokasi_gambar_terenkripsi = "./input/"+ input_gambar +".tiff";
    lokasi_gambar_terdekripsi = "./output/"+ output_gambar +".tiff";

    n_bits = 3;

    gambar_yang_didekripsi = Image.open(lokasi_gambar_terenkripsi);
    dekripsi(gambar_yang_didekripsi, n_bits).save(lokasi_gambar_terdekripsi);
