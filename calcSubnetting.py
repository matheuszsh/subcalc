from calcCIDR import cidrToMask
import ipaddress
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Subnetwork calculation tool")
    parser.add_argument('-ip', '--internet-address', type=str, help='use this option to specify the ip address.')
    parser.add_argument('-mc', '--main-cidr', type=int, help='use this option to specify the main net cidr')
    parser.add_argument('-sc', '--sub-cidr', type=int, help='use this option to specify the subnet cidr')

    args = parser.parse_args()

    obj_net = NetBuilder(args.internet_address, args.main_cidr, args.sub_cidr)

    print(obj_net.show_subnet_data())
    obj_net.generete_subnets()


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

        return (f"IP: {self.this_main_net}/{self.this_main_net_cidr}\n"
                f"Mascara: {self.main_net_mask}\n"
                f"Total IPs: {total_net_ip}\n"
                f"Hosts válidos: {total_net_ip - 2}\n"
                f"Rede: 1\n"
                f"Broadcast: 1\n"
                f"Bits para hosts: {32 - self.this_main_net_cidr}"
        )

    def show_subnet_data(self):

        total_subnet_ip = 2 ** (32 - self.this_sub_net_cidr)

        total_nets = int((2 ** (32 - self.this_main_net_cidr)) / (2 ** (32 - self.this_sub_net_cidr)))

        return (
            f"IP: {self.this_main_net}/{self.this_sub_net_cidr}\n"
            f"Mascara: {self.sub_net_mask}\n"
            f"Total redes: {total_nets}\n"
            f"Total IPs por host: {total_subnet_ip}\n"
            f"Hosts total por rede: {total_subnet_ip - 2}\n"
            f"Rede para bit: 1\n"
            f"Broadcast para bit: 1\n"
            f"Bits para hosts: {32 - self.this_sub_net_cidr}"
        )

    def generete_subnets(self):

        # Constructor object main net
        main_net_g = ipaddress.IPv4Network(f"{self.this_main_net}/{self.this_main_net_cidr}", strict=False)

        if self.this_sub_net_cidr <= self.this_main_net_cidr:
            print("O CIDR de subredes é maior ou igual ao da rede principal.")
            return

        # Generete subnets to main_net_g
        subnetlist = list(main_net_g.subnets(new_prefix=self.this_sub_net_cidr))

        subnet_v = 0

        print("<><><><><><><><>|LISTA DE SUBREDES|<><><><><><><><> ")
        # enumerate return an index and an object
        for i,net in enumerate(subnetlist):
            print(f"------REDE {i}------")
            print(f"REDE: {net.network_address}")
            print(f"BROADCAST: {net.broadcast_address}")
        
    
if __name__ == "__main__":
    main()