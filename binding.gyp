{
    "targets": [{
        "target_name": "lwip_decoder",
        "sources": [
            # LWIP:
            #######
            "src/decoder/init.cpp",
            "src/decoder/util.cpp",
            "src/decoder/buffer_worker.cpp",
            "src/decoder/jpeg_decoder.cpp",
            "src/decoder/png_decoder.cpp",
            "src/decoder/gif_decoder.cpp",
            # LIB JPEG:
            ###########
            "src/lib/jpeg/jmemnobs.c",
            "src/lib/jpeg/jcomapi.c",
            "src/lib/jpeg/jdapimin.c",
            "src/lib/jpeg/jdapistd.c",
            "src/lib/jpeg/jdatadst.c",
            "src/lib/jpeg/jdatasrc.c",
            "src/lib/jpeg/jdcoefct.c",
            "src/lib/jpeg/jdcolor.c",
            "src/lib/jpeg/jddctmgr.c",
            "src/lib/jpeg/jdhuff.c",
            "src/lib/jpeg/jdinput.c",
            "src/lib/jpeg/jdmainct.c",
            "src/lib/jpeg/jdmarker.c",
            "src/lib/jpeg/jdmaster.c",
            "src/lib/jpeg/jdpostct.c",
            "src/lib/jpeg/jdsample.c",
            "src/lib/jpeg/jerror.c",
            "src/lib/jpeg/jfdctflt.c",
            "src/lib/jpeg/jfdctfst.c",
            "src/lib/jpeg/jfdctint.c",
            "src/lib/jpeg/jidctflt.c",
            "src/lib/jpeg/jidctfst.c",
            "src/lib/jpeg/jidctint.c",
            "src/lib/jpeg/jutils.c",
            "src/lib/jpeg/jmemmgr.c",
            "src/lib/jpeg/jdarith.c",
            "src/lib/jpeg/jdmerge.c",
            "src/lib/jpeg/jaricom.c",
            "src/lib/jpeg/jquant1.c",
            "src/lib/jpeg/jquant2.c",
            # LIB PNG:
            ##########
            "src/lib/png/png.c",
            "src/lib/png/pngset.c",
            "src/lib/png/pngget.c",
            "src/lib/png/pngrutil.c",
            "src/lib/png/pngtrans.c",
            "src/lib/png/pngread.c",
            "src/lib/png/pngrio.c",
            "src/lib/png/pngrtran.c",
            "src/lib/png/pngmem.c",
            "src/lib/png/pngerror.c",
            "src/lib/png/pngpread.c",
            # ZLIB:
            #######
            "src/lib/zlib/adler32.c",
            "src/lib/zlib/crc32.c",
            "src/lib/zlib/gzlib.c",
            "src/lib/zlib/gzread.c",
            "src/lib/zlib/infback.c",
            "src/lib/zlib/inflate.c",
            "src/lib/zlib/inftrees.c",
            "src/lib/zlib/inffast.c",
            "src/lib/zlib/uncompr.c",
            "src/lib/zlib/zutil.c",
            "src/lib/zlib/trees.c",
            # LIB GIF:
            ##########
            "src/lib/gif/dgif_lib.c",
            "src/lib/gif/gif_err.c",
            "src/lib/gif/gifalloc.c",
        ],
        'include_dirs': [
            '<!(node -e "require(\'nan\')")',
            'src/decoder',
            'src/lib/zlib',
            'src/lib/jpeg',
            'src/lib/cimg',
            'src/lib/png',
            'src/lib/gif'
        ],
        'conditions': [
            ['OS=="freebsd"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="solaris"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="linux"', {
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                },
                'include_dirs': ['/usr/include/malloc']
            }],
            ['OS=="win"', {
                'configurations': {
                    'Release': {
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'ExceptionHandling': 1
                            }
                        }
                    }
                },
                'include_dirs': ['src/win']
            }]
        ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }]
}
