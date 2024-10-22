from Crypto.Util.number import long_to_bytes, inverse, bytes_to_long
import math

# GIGEM 
pNON = 9942564401124784370817949981506109463550890467971163846364245914543686506095700362448364280259029479542280541985520857408286580088352541049846554629477137
kNON = 9301568977067599595794917435536322072979096972667835027052777328667056134966201698148663065711079784539030845611119652110075758146440790725325026976284542
mNON = "3b36c26da3b8463cce58f721f1e473e160b5be35dc6a6452331bda164bbc7025a9f3f2cdf8ef7e991b5bdb9a19863d05a15102648efa65087cf08764418f0218"
encryptEX = "8db305833963c26a2c2c157b13d2319150d362f9fe69f9e5b2ea52a88b1e66e023e5f0216165d098ad395d2ab25432f7cab2b31688d2aa396a433b93815d5ac4"
encryptB = "7a1f722ad939ae60100e97aabff36bbdd20f14724cc36d32044ac841b1b5f62ee7b311f88a3421b70852eaf43161ad3b920446492ddfb2227ea36b44584ac6d1"
encryptc = "4aa4aba3e5a9fed65e480b627856e01e44d4ccfbe59f64c6e5753244401dc853d54c17d33c4966a16ff1edc2a8eb2c4ffebf5b30efa9b6838780521f9e8cec"
EXLONG = int.from_bytes(bytes.fromhex("a5a1c15739d0129cd09dcdb03c828d170ad33e3b45ca7ee16b30a7ad28b132b861fe298fe2e1568e5334705adc82b4a0e58cacfaafe41535beb2a7b8e543f340"))
BLONG = int.from_bytes(bytes.fromhex("8d6d449ccf536dcbd7329aa96218d9e14a342c28c047e903ada0542357d8e9e4172cb1ded956e93dbae6da0b6146d034e55835dfb0cf906ba5adbaa9123c536f"))
cLONG = int.from_bytes(bytes.fromhex("7538c7e264d6c8faddc767a287af26ab89951a163ac55325f01000998700a10fcc5b3a2dcfcc7bed229943bbe60aebc8e523bec4b1bb0ba18ca8cd993f34b39e"))
# Assuming you have p, k, and Cflag already:
# p = the 512-bit prime used in encryption
# k = the key used in encryption
# Cflag_hex = the encrypted flag in hexadecimal form

# Convert the hexadecimal Cflag to an integer
inCflag = bytes.fromhex("a0bc2e6c72b43c0b913fc5a2108541c0d780195a4b6cdca36c07e37752cf73d9a31463225ee6d231a7fae63cbdce408dfb6930478283d267f718ac806cb45124")
Cflag = int.from_bytes(inCflag, "big")
p = math.gcd((3 * EXLONG) - cLONG, (2 * EXLONG) - BLONG)

m_inv = inverse(bytes_to_long("!".encode()), p)
kMOD = (EXLONG * m_inv) % p
print(kMOD)

k_inv = inverse(kNON, pNON)
m = (Cflag * k_inv) % pNON
decrypted_flag = long_to_bytes(m)
print(decrypted_flag.decode())