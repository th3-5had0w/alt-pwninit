import patch_elf,Libc,argparse
from pwn import ELF
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--bin",metavar="<Bin file>",help="<Binary to pwn>",required=True)
    parser.add_argument("-l","--libc",metavar="<Libc file>",help="<Challenge libc>",required=True)
    parser.add_argument("--ld",help="<A linker to preload the libc> (Optional)")
    args = parser.parse_args()
    if (not args.bin) or (not args.libc) :
        return 1
    file_bin=ELF(args.bin)  #Check bin is a valid ELF ?
    file_libc=Libc.LIBC(args.libc) #Check bin is a valid LIBC ?
    if args.ld:
        file_ld=ELF(args.ld,checksec=0)
    else:
        file_ld=Libc.get_ld(file_libc)
    Libc.unstrip(file_libc)
    Libc.unstrip_ld(file_libc,file_ld)
    patch_elf.patch(file_bin,file_libc,file_ld)

if __name__=='__main__':
    main()
