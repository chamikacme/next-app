
import Image from "next/image";
import {
    BellIcon,
    ChatIcon,
    ChevronDownIcon,
    HomeIcon,
    UserGroupIcon,
    ViewGridAddIcon,
} from "@heroicons/react/solid";
import {
    FlagIcon,
    PlayIcon,
    ShoppingCartIcon,
    SearchIcon 

} from "@heroicons/react/outline"

function Header(){
    return(
        <div>
           {/* Left */}
           <div className="flex items-center">
               <Image
               src = "https://links.papareact.com/5me"
               width={40}
               height={40}
               layout="fixed"
               />

               <div className="flex ml-2 items-center bg-gray-100 rounded-full p-2">
                   <SearchIcon className="h-6 text-gray-600"/>
                   <input type="text" placeholder="Search" className="hidden md:inline-flex ml-2 items-center"/>

               </div>
           </div>
           {/* Center */}

           {/* Right */}

        </div>
    )
}

export default Header