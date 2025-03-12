#!/usr/bin/env python3

from calcCIDR import cidrToMask
import ipaddress
from argparse import ArgumentParser

def main():
    try:
        parser = ArgumentParser(description="Subnetwork calculation tool")
        parser.add_argument('-ip', '--internet-address', type=str, required=True, help='use this option to specify the ip address.')
        parser.add_argument('-mc', '--main-cidr', type=int, required=True, help='use this option to specify the main net cidr')
        parser.add_argument('-sc', '--sub-cidr', type=int, required=True, help='use this option to specify the subnet cidr')
        parser.add_argument('-vmc', '--verbose-maincidr', action='store_true', help='use this option to show the subnet cidr data')
        parser.add_argument('-vsc', '--verbose-subcidr', action='store_true', help='use this option to show the subnet cidr data')

        args = parser.parse_args()

        obj_net = NetBuilder(args.internet_address, args.main_cidr, args.sub_cidr)

        if args.verbose_maincidr:
            obj_net.show_main_net_data()
        if args.verbose_subcidr:
            obj_net.show_subnet_data()

        if args.verbose_maincidr == False and args.verbose_subcidr == False:
            print("DISPLAY OTHER MODES\n\n"
              "-vmc, --verbose-maincidr, use this option to show the main net cidr data\n\n"
              "-vsc, --verbose-subcidr, use this option to show the subnet cidr data\n\n"
              )

        obj_net.generete_subnets()
        
    except:
        print("usage subcalc compile: subcalc -ip <ip address> -mc <CIDR main net> -sc <CIDR subnet>")


class NetBuilder:
    def __init__(self,main_net : str, main_net_cidr : int, sub_net_cidr : int):
        self.this_main_net = main_net
        self.this_main_net_cidr = main_net_cidr
        self.this_sub_net_cidr = sub_net_cidr
        # CIDR Convert
        self.main_net_mask = cidrToMask(main_net_cidr)
        self.sub_net_mask = cidrToMask(sub_net_cidr)


    def __str__(self):
        return f""
    
    def show_main_net_data(self):

        total_net_ip = 2 ** (32 - self.this_main_net_cidr)

        print (f"\n------------MAIN NET CIDR--------\n\n"
            f"IP: {self.this_main_net}/{self.this_main_net_cidr}\n"
            f"Netmask: {self.main_net_mask}\n"
            f"Total Ips: {total_net_ip}\n"
            f"Hosts available: {total_net_ip - 2}\n"
            f"Network: 1\n"
            f"Broadcast: 1\n"
            f"Bits to hosts: {32 - self.this_main_net_cidr}"
        )

    def show_subnet_data(self):

        total_subnet_ip = 2 ** (32 - self.this_sub_net_cidr)

        total_nets = int((2 ** (32 - self.this_main_net_cidr)) / (2 ** (32 - self.this_sub_net_cidr)))

        print (f"\n-----------SUBNET CIDR-----------\n\n"
            f"IP: {self.this_main_net}/{self.this_sub_net_cidr}\n"
            f"Netmask: {self.sub_net_mask}\n"
            f"Total networks: {total_nets}\n"
            f"Total ip per networks: {total_subnet_ip}\n"
            f"Total host per networks: {total_subnet_ip - 2}\n"
            f"Network: 1\n"
            f"Broadcast: 1\n"
            f"Bits to hosts: {32 - self.this_sub_net_cidr}\n"
        )

    def generete_subnets(self):

        # Constructor object main net
        main_net_g = ipaddress.IPv4Network(f"{self.this_main_net}/{self.this_main_net_cidr}", strict=False)

        if self.this_sub_net_cidr <= self.this_main_net_cidr:
            print("\nERRO:The CIDR of subnets is less than or equal to that of the main network CIDR.\n")
            return

        # Generete subnets to main_net_g
        subnetlist = list(main_net_g.subnets(new_prefix=self.this_sub_net_cidr))

        subnet_v = 0

        print("<><><><><><><><>|SUBNET LIST|<><><><><><><><> ")
        # enumerate return an index and an object
        for i,net in enumerate(subnetlist):
            print(f"\n------NETWORK {i+1}------")
            print(f"NETWORK: {net.network_address}")
            print(f"HOST: {net.network_address + 1} - {net.broadcast_address - 1}")
            print(f"BROADCAST: {net.broadcast_address}")
        
    
if __name__ == "__main__":
    main()