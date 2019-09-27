echo "Installing capnp"

cd
VERSION=0.6.1
wget https://capnproto.org/capnproto-c++-${VERSION}.tar.gz
tar xvf capnproto-c++-${VERSION}.tar.gz
cd capnproto-c++-${VERSION}
CXXFLAGS="-fPIC" ./configure --prefix=/data/data/com.termux/files/usr

make -j4 && make install

# manually build binaries statically
g++ -std=gnu++11 -I./src -I./src -DKJ_HEADER_WARNINGS -DCAPNP_HEADER_WARNINGS -DCAPNP_INCLUDE_DIR=\"/data/data/com.termux/files/usr/local/include\" -pthread -O2 -DNDEBUG -pthread -pthread -o .libs/capnp src/capnp/compiler/module-loader.o src/capnp/compiler/capnp.o  ./.libs/libcapnpc.a ./.libs/libcapnp.a ./.libs/libkj.a -lpthread -pthread

g++ -std=gnu++11 -I./src -I./src -DKJ_HEADER_WARNINGS -DCAPNP_HEADER_WARNINGS -DCAPNP_INCLUDE_DIR=\"/data/data/com.termux/files/usr/local/include\" -pthread -O2 -DNDEBUG -pthread -pthread -o .libs/capnpc-c++ src/capnp/compiler/capnpc-c++.o  ./.libs/libcapnp.a ./.libs/libkj.a -lpthread -pthread

g++ -std=gnu++11 -I./src -I./src -DKJ_HEADER_WARNINGS -DCAPNP_HEADER_WARNINGS -DCAPNP_INCLUDE_DIR=\"/data/data/com.termux/files/usr/local/include\" -pthread -O2 -DNDEBUG -pthread -pthread -o .libs/capnpc-capnp src/capnp/compiler/capnpc-capnp.o  ./.libs/libcapnp.a ./.libs/libkj.a -lpthread -pthread

cp .libs/capnp /data/data/com.termux/files/usr/bin/
ln -s /usr/bin/capnp /data/data/com.termux/files/usr/bin/capnpc
cp .libs/capnpc-c++ /data/data/com.termux/files/usr/bin/
cp .libs/capnpc-capnp /data/data/com.termux/files/usr/bin/
cp .libs/*.a /data/data/com.termux/files/usr/lib


#ln -s /data/data/com.termux/files/usr/bin/capnp /data/data/com.termux/files/usr/bin/capnpc


cd
echo "Installing c-capnp"
git clone https://github.com/zorrobyte/c-capnproto.git
cd c-capnproto
git submodule update --init --recursive
autoreconf -f -i -s
CXXFLAGS="-fPIC" ./configure --prefix=/data/data/com.termux/files/usr
make -j4 && make install

# manually build binaries statically
gcc -fPIC -o .libs/capnpc-c compiler/capnpc-c.o compiler/schema.capnp.o compiler/str.o  ./.libs/libcapnp_c.a

cp .libs/capnpc-c /data/data/com.termux/files/usr/bin/
cp .libs/*.a /data/data/com.termux/files/usr/lib
