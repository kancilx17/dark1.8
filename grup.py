# uncompyle6 version 3.4.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul 28 2019, 22:06:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys, time, json, requests
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'

def id_member():
    print
    idmem = []
    try:
        os.mkdir('dump')
    except OSError:
        pass
    else:
        idg = raw_input(tutup + '[' + lime + '+' + tutup + '] Input ID Group : ' + lime)
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + token)
            s = json.loads(r.text)
            print tutup + '[' + blue + './' + tutup + '] Name Group : ' + lime + s['name'] + tutup
        except KeyError:
            print tutup + '[' + merah + '!' + tutup + '] Group Not Found'
            exit()

        try:
            print tutup + '[' + lime + '+' + tutup + '] Fetching id from member group ...' + tutup
            save = open('dump/id_member.txt', 'w')

            def lanjut(urlz):
                u = requests.get(urlz)
                hasil = json.loads(u.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')
                    print tutup + '\r[' + lime + '+' + tutup + '] Total : ' + str(len(idmem)),
                    sys.stdout.flush
                    time.sleep(0.0001)

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return

            def ambil():
                r = requests.get('https://graph.facebook.com/' + idg + '/members?fileds=id&limit=5000&summary=true&access_token=' + token)
                hasil = json.loads(r.text)
                halaman = hasil['paging']
                for z in hasil['data']:
                    idmem.append(z['id'])
                    save.write(z['id'] + '\n')

                if halaman.get('next') is not None:
                    lanjut(halaman.get('next'))
                return

            ambil()
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] Successfully get id from member group'
            done = raw_input(tutup + '[' + lime + '+' + tutup + '] Save file with name : ' + lime)
            print tutup + '[' + lime + '+' + tutup + '] Create file ...'
            time.sleep(2)
            os.rename('dump/id_member.txt', 'dump/' + done)
            print tutup + '[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/' + done + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            exit()
        except (KeyboardInterrupt, IOError, EOFError, KeyError):
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            exit()
        except requests.exceptions.ConnectionError:
            save.close()
            print tutup + '\n[' + lime + '+' + tutup + '] File saved : ' + lime + 'dump/id_member.txt' + tutup
            print tutup + '[' + lime + '+' + tutup + '] Selesai ^-^'
            exit()


try:
    token = open('logs.txt', 'r').read()
    id_member()
except (KeyError, IOError):
    os.system('clear')
    print 'Token not found !'