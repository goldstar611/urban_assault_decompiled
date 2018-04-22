import compile
import struct


# https://github.com/Marisa-Chan/UA_source/blob/master/src/particle.cpp#L681
def main():
    # mfile->readS16B(atts.version);
    #
    # Vec3dReadIFF(atts.accel.start, mfile, true);
    # Vec3dReadIFF(atts.accel.end, mfile, true);
    # Vec3dReadIFF(atts.magnify.start, mfile, true);
    # Vec3dReadIFF(atts.magnify.end, mfile, true);
    #
    # mfile->readS32B(atts.collide);
    # mfile->readS32B(atts.startSpeed);
    # mfile->readS32B(atts.contextNumber);
    # mfile->readS32B(atts.contextLifeTime);
    # mfile->readS32B(atts.contextStartGen);
    # mfile->readS32B(atts.contextStopGen);
    # mfile->readS32B(atts.genRate);
    # mfile->readS32B(atts.lifeTime);
    # mfile->readS32B(atts.startSize);
    # mfile->readS32B(atts.endSize);
    # mfile->readS32B(atts.noise);

    chunk = compile.Atts().load_from_file("ATTS.ptcl")
    data = chunk.chunk_data

    print(len(data))

    (version,
     accel_start_x, accel_start_y, accel_start_z,
     accel_end_x, accel_end_y, accel_end_z,
     magnify_start_x, magnify_start_y, magnify_start_z,
     magnify_end_x, magnify_end_y, magnify_end_z,
     collide, start_speed,
     context_number, context_life_time,
     context_start_gen, context_stop_gen,
     gen_rate, lifetime,
     start_size, end_size, noise) = struct.unpack(">hfffffffffffflllllllllll", data)


if __name__ == '__main__':
    main()
